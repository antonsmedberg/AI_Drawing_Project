import tkinter as tk
from AIInterface import AIInterface
from model import Model
from data import load_dataset

def main():
    try:
        # Initialize the Tkinter root window
        root = tk.Tk()
        root.title("AI Feedback Tool")  # Set the title of the window

        # Initialize AI interface
        app = AIInterface(root)
        
        # Initialize model
        model = Model()
        
        # Load dataset
        train_directory = "C:/Users/Anton/OneDrive/Desktop/AI_Drawing_Project/dataset/train"
        validate_directory = "C:/Users/Anton/OneDrive/Desktop/AI_Drawing_Project/dataset/validate"
        X_train, y_train = load_dataset(train_directory)
        X_validate, y_validate = load_dataset(validate_directory)
        
        # Hyperparameters
        num_epochs = 10
        batch_size = 32
        
        # Initialize training progress history
        loss_history = []
        accuracy_history = []
        
        # Train the model
        for epoch in range(num_epochs):
            print("Epoch:", epoch)
            # Perform one epoch of training on the training dataset
            for i in range(0, len(X_train), batch_size):
                X_batch = X_train[i:i+batch_size]
                y_batch = y_train[i:i+batch_size]
                train_loss, train_accuracy = model.train_on_batch(X_batch, y_batch)
                loss_history.append(train_loss)
                accuracy_history.append(train_accuracy)
            
            # Validate the model on the validation dataset
            validate_loss, validate_accuracy = model.evaluate(X_validate, y_validate)
            
            # Update the training progress in the UI
            app.show_training_progress(loss_history, accuracy_history, validate_loss, validate_accuracy)
            
            # Generate a drawing
            drawing = model.generate_drawing()
            
            # Display the drawing in the UI
            app.display_generated_drawing(drawing)
            
            # Get user feedback from the UI
            user_feedback = app.get_user_feedback()
            
            if user_feedback == "retry":
                # Retry drawing generation
                continue
            elif user_feedback == "accept":
                # Add the drawing to the dataset and retrain the model
                for i in range(0, len(X_train), batch_size):
                    X_batch = X_train[i:i+batch_size]
                    y_batch = y_train[i:i+batch_size]
                    model.train_on_batch(X_batch, y_batch)  # Retrain the model with the updated dataset
            elif user_feedback == "quit":
                # Exit the program
                break
                
        root.mainloop()  # Start the Tkinter event loop

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()