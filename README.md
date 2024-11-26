# StudyCraft

<p align="center">
  <img src="https://github.com/Emanalytics7/StudyCraft/blob/main/artifacts/swan.png" alt="StudyCraft Logo" width="150"/>
</p>

<h2 align="center">Your Personal AI Study Buddy</h2>

<p align="center">
  👉 <a href="https://study-craft.streamlit.app/">Try StudyCraft Now!</a>

## What is StudyCraft?

StudyCraft is a web application that creates a personalized learning schedule of your preferred style and generates a comprehensive PDF of the plan.

### See StudyCraft in Action

https://github.com/user-attachments/assets/b950d6c2-04ec-42dc-8c1d-38804115e91f


## Features

- **Custom Study Plans**: Tailored just for you and your learning style
- **AI-Powered Content**: Uses smart AI to create study materials
- **Resource Finder**: Automatically finds and includes helpful resources
- **PDF Magic**: Turns your study plan into a neat, downloadable PDF

## Tech Stack

- **[Groq API](https://console.groq.com/)**: Powers our smart AI brain (Llama3-70b)
- **[Exa API](https://exa.ai/)**: Helps find the best study resources
- **Google Fonts**: Makes your study plan look cool (i used "Anonymous Pro")

## File Structure 
```plaintext
StudyCraft/
│
├── artifacts/               # Contains generated PDFs and other output files
│   ├── example_output.pdf
│   └── ...
│
├── fonts/                   # Includes custom fonts used in PDF generation
│   ├── AnonymousPro-Regular.ttf
│   └── ...
│  
├── app.py                   # Main Streamlit application file
│                            
├── content_generation.py   # Contains the main logic for generating content based on user input and templates.
│                      
│
├── pdf_conversion.py       # Uses ReportLab to style and compile the final PDF documents.                           
│
└── prompt_template.txt      # Template for AI content generation prompts
```

## Getting Started

### What You'll Need

- Python 3.10 or newer
- Groq & Exa API keys (optional, in case my apis dont work!)

### Setup Steps

1. **Grab the Code**
   ```bash
   git clone https://github.com/Emanalytics7/StudyCraft.git
   cd StudyCraft
   ```
2. **Install the Dependencies**
  ```bash
pip install -r requirements.txt
  ```
3. **Set Up Your API Keys**
   Create a .env file and add your API keys (if you have them)

4. **Launch StudyCraft**
  ```bash
streamlit run app.py
  ```

## How to Use
- Open StudyCraft in your browser
- Tell it your study goals and how you like to learn
- Click to generate your personalized study plan
- Download your new PDF and start learning!

## Contribute
I'd love your help to make StudyCraft even better!

## How to Join In
- Fork the project
- Create your feature branch `(git checkout -b feature/AmazingFeature)`
- Commit your changes `(git commit -m 'Add some AmazingFeature')`
- Push to the branch `(git push origin feature/AmazingFeature)`
- Open a Pull Request

## Ideas for Improvement
- Progress trackers and charts
- More advanced AI study content
- Links to additional learning resources
- Customizable PDF themes and layouts

## License
This project is under the MIT License. Check out the LICENSE file for the legal details.

*If you found StudyCraft helpful & amazing, please give it a star! ⭐
This was a fun project I did just for fun, and I hope you like it* 

---

<p align="center">
  Made with ❤️ by Eman | © 2024 StudyCraft
</p>
<p align="center">
  <a href="https://www.linkedin.com/in/eman-nisar/">LinkedIn</a> •
</p>

