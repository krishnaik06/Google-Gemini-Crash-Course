# Food Label Translation from English to Hindi using Google Gemini Pro Vision API

## Introduction

This project is an extension of Krish Naik's Google Gemini Crash Course. The project aims to translate the food labels from English to Hindi using the Google Gemini Pro Vision API. The project is divided into two parts. Through streamlit, the user can upload the image, which is sent to the Google Gemini Pro Vision API. The vision transformer performs its magic and returns the nutrition as well ingredients of the food label in Hindi. Through some prompt engineering, the user also obtains home-cooked alternatives to unhealthy products in Hindi.

## Installation

The project requires the following packages:

```bash
pip install streamlit
pip install google-generativeai
pip install python-dotenv
```

Or you can install the packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

## Usage

To run the project, use the following command:

```bash
streamlit run app.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

GNU GENERAL PUBLIC LICENSE

## Project Status

The project is currently under development. I aim to add more features to the project, such as telemetry. Possibly converting the project into a mobile application using Flutter or React Native is also on the cards.
