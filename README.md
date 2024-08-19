
# Prompt Safe

This Flask web application allows users to register, submit feedback, and evaluate inputs for potential prompt injections using Google’s Gemini AI model. The app is designed to analyze user prompts against predefined datasets related to sales transactions, system prompts, and invoice manipulation, ensuring that prompts do not manipulate or alter model behavior inappropriately.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Deployment on Vercel](#deployment-on-vercel)
6. [Usage](#usage)
7. [License](#license)

## Features

- **User Registration & Feedback**: Users can register with their name and email, and submit feedback.
- **Prompt Injection Detection**: The app uses the Gemini AI model to evaluate if user inputs are related to prompt injections within specific contexts.
- **Dataset Integration**: Three PDF datasets are used to check for prompt injections related to transactions, system prompts, and invoices.
- **Database Management**: User data and feedback are stored and managed using SQLAlchemy and SQLite.
- **Custom Error Handling**: Includes custom 404 and 500 error pages for improved user experience.
- **Deployment**: Configured for deployment on Vercel, ensuring a smooth and scalable deployment process.

## Technologies Used

- **Flask**: Web framework for building the app.
- **Flask-WTF**: For form handling and validation.
- **Flask-SQLAlchemy**: ORM for database management.
- **Google Generative AI (Gemini Model)**: For evaluating user prompts.
- **PyPDF2**: For extracting text from PDF datasets.
- **Vercel**: Deployment platform.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/prompt-injection-detector.git
   cd prompt-injection-detector
   ```

2. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the SQLite database:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

4. **Run the app:**
   ```bash
   flask run
   ```

## Configuration

- **Database**: The app uses SQLite by default. Ensure that the `SQLALCHEMY_DATABASE_URI` in `app.config` is set to the correct database path.
- **Google API Key**: Set your Google API key for the Gemini model in the environment variables.

## Deployment on Vercel

1. **Install the Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy the app:**
   ```bash
   vercel --prod
   ```

3. **Configure `vercel.json`:**
   Ensure your `vercel.json` file is correctly configured to handle the Python serverless function.

## Usage

- Navigate to `User` to register and submit feedback.
- Use the form on `Evaluate` to evaluate prompts for potential injection.
- View registered users and their feedback in the `Users` section.
- To Know about Prompt-Injection click 'Article'.

The Videographic representation of the web-app UI:


https://github.com/user-attachments/assets/ada78abf-04bb-4d0f-aa53-cbfc9b55e8b0


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

This index will help users quickly navigate through the different sections of your `README` file.
