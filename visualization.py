# visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_data(loss_history, accuracy_history=None, title='Träningsframsteg'):
    sns.set()  # Använder Seaborn's standardteman för att göra plottarna snyggare
    fig, ax1 = plt.subplots()

    # Konfigurerar den primära axeln för förlust
    color = 'tab:red'
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Förlust', color=color)
    ax1.plot(loss_history, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    # Konfigurerar en sekundär axel för noggrannhet om sådan data finns
    if accuracy_history:
        ax2 = ax1.twinx()
        color = 'tab:blue'
        ax2.set_ylabel('Noggrannhet', color=color)
        ax2.plot(accuracy_history, color=color)
        ax2.tick_params(axis='y', labelcolor=color)

    plt.title(title)
    fig.tight_layout()
    plt.show()

def show_drawing_with_feedback(drawing):
    plt.imshow(drawing, cmap='gray')
    plt.title('Genererad Teckning')
    plt.axis('off')  # Gömmer axlarna för en renare bild
    plt.show()

