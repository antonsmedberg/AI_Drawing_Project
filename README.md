
# AI Feedback Tool

## Introduction
AI Feedback Tool är designat för att underlätta träningen och utvärderingen av AI-modeller med användarfeedback. Detta verktyg erbjuder en interaktiv plattform där användare kan ge feedback på AI-genererade bilder, vilket hjälper till att finjustera modellens prestationer.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Training with Your Own Dataset](#training-with-your-own-dataset)
  - [Using a Pre-Trained Model](#using-a-pre-trained-model)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Features
- **Användargränssnitt (AIInterface):** Ett interaktivt gränssnitt för att ge feedback på AI-genererade teckningar.
- **Canvas för teckning:** Möjlighet för användaren att rita och interagera direkt med AI-modellen.
- **Feedback-kontroller:** Användare kan enkelt ge feedback genom att klicka på "Ja" eller "Nej".
- **Modellkontroller:** Spara och ladda tränade modeller för återanvändning.
- **Datahantering:** Effektiv inläsning och förberedelse av träningsdata.
- **Visualisering:** Visualisera träningsframsteg inklusive förlust och noggrannhet.

## Installation
```bash
git clone https://github.com/antonsmedberg/AI_Drawing_Project
cd ditt-projekt
```

## Usage

### Training with Your Own Dataset
1. Förbered ditt träningsdataset i undermappar för träning och validering.
2. Justera hyperparametrar i `main.py`.
3. Kör `main.py` för att starta träningen.
4. Spara den tränade modellen via användargränssnittet.

### Using a Pre-Trained Model
1. Ladda ner en färdigtränad modell.
2. Kopiera modellen till `results`-mappen.
3. Kör `main.py` för att starta och använda modellen.
4. Ge feedback och tolka resultat genom samma interaktionsflöde.

## Dependencies
Se till att ha Python och alla nödvändiga bibliotek installerade. Lista alla bibliotek och versioner här.

## Configuration
Beskriv hur man konfigurerar hyperparametrar och andra inställningar i `main.py` eller andra relevanta filer.

## Documentation
Länk till ytterligare dokumentation om det finns.

## Examples
Inkludera exempel på användning, skärmbilder eller kodblock här.

## Troubleshooting
Vanliga problem och deras lösningar.

## Contributors
Lista över personer som har bidragit till projektet.

## License
Ange licensinformation här. Exempel: MIT, GPL, etc.
