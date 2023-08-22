import streamlit as st
import time
from PIL import  Image
import os


def main():
    st.set_page_config(page_title="Animesh portfolio App", page_icon=":smiley:",layout="wide",initial_sidebar_state="expanded")



    st.toast("please open the website in desktop site mode for better display")
    st.markdown(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">',
        unsafe_allow_html=True)

    # Sidebar navigation panel

    navigation_options = ["Home", "Projects", "Resume"]
    selected_option = st.sidebar.selectbox("Go to", navigation_options)

    # Display content based on selected option
    if selected_option == "Home":
        show_home_page()
    elif selected_option == "Projects":
        show_projects_page()
    elif selected_option == "Resume":
        show_resume_page()

    st.sidebar.title("Contact me:")
    linkedin_profile = "https://www.linkedin.com/in/your_linkedin_profile/"
    github_profile = "https://github.com/iamanimesh11"
    gmail_address = "iamanimesh11june@gmail.com"

    linkedin_icon_data = image_to_base64(Image.open("icons/linkedin.png"))
    github_icon_data = image_to_base64(Image.open("icons/github.png"))
    gmail_icon_data = image_to_base64(Image.open("icons/gmail.png"))

    icon_size = "50px"
    icon_margin = "10px"

    css_style = '''
            .icon:hover {
                transform: scale(1.2);
            }
        '''

    linkedin_icon = f'<a href="{linkedin_profile}" target="_blank"><img src="data:image/png;base64,{linkedin_icon_data}" class="icon" width="{icon_size}" height="{icon_size}" style="margin-bottom:{icon_margin};"></a>'
    github_icon = f'<a href="{github_profile}" target="_blank"><img src="data:image/png;base64,{github_icon_data}" class= "icon" width="{icon_size}" height="{icon_size}"style= border-radius:10px;background-color:white;"margin-bottom:{icon_margin};"></a>'
    gmail_icon = f'<a href="mailto:{gmail_address}" target="_blank"><img src="data:image/png;base64,{gmail_icon_data}" class= "icon" width="{icon_size}" height="{icon_size}"style="margin-bottom:{icon_margin};"></a>'

    st.markdown(f'<style>{css_style}</style>', unsafe_allow_html=True)

    st.sidebar.markdown(
        f'<div style="display: flex; flex-direction: column; align-items: center;">{linkedin_icon}{github_icon}{gmail_icon}</div>',
        unsafe_allow_html=True)

def show_home_page():
    glowing_text_css = """
        .glowing-text {
            font-size: 30px;
            font-weight: bold;
            color: #ffffff;
            text-shadow: 0 0 10px rgba(0, 255, 0, 0.8),
                         0 0 15px rgba(0, 255, 153, 0.8),
                         0 0 20px rgba(0, 153, 255, 0.8),
                         0 0 25px rgba(153, 0, 255, 0.8),
                         0 0 30px rgba(255, 0, 255, 0.8),
                         0 0 35px rgba(255, 0, 102, 0.8);
        }
    """


    left_column, right_column = st.columns(2)

    image = Image.open("unnamed-removebg-preview-modified.png")
    image_html = f"<img src='data:image/png;base64,{image_to_base64(image)}' " \
                 f"style='border: 2px solid #ffffff; border-radius: 160px; box-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 40px #00ff00;' " \
                 f"width='300' alt='Beautiful Image'>"
    left_column.markdown(image_html, unsafe_allow_html=True)

    styled_text = """
        <style>
            .description {
                font-size: 24px;
                color: #ffffff;
                line-height: 1.6;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                margin-bottom: 20px;
            }
            .role {
                font-size: 36px;
                font-weight: bold;
                color: #00ff99;
                background: linear-gradient(90deg, #00ff99, #33ccff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .eye-catching-text {
                font-size: 48px;
                font-weight: bold;
                color: #ff0066;
                text-shadow: 2px 2px 4px rgba(255, 0, 102, 0.8);
                margin-bottom: 10px;
            }
            .name-container {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .name {
                font-size: 60px;
                font-weight: bold;
                font-family: "Pacifico", cursive;
                background: linear-gradient(45deg, #ff5f6d, #ff9970);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .hello-text {
                font-size: 32px;
                font-weight: bold;
                font-family: "Candara", sans-serif;
                color: #00ff99;
                margin: 0;
            }
        </style>
        <div style='text-align: center;'>
            <div class="name-container">
                <h4 class="hello-text">
                    Hello, I am
                </h4>
                <h1 class="name">
                    <span class="name">Animesh Singh</span>
                </h1>
            </div>
            <p class="description">
                I am a <span class="role">Data Scientist</span>, <span class="role">AI Enthusiast</span>, and <span class="role">RPA Developer</span>
                with a passion for leveraging data and technology to drive innovation.
            </p>
            <p class="quote">
                "The only way to do great work is to love what you do." - Steve Jobs
            </p>
            <p class="description">
                Let's collaborate and build <span class="role">amazing</span> solutions together!
            </p>
        </div>
    """

    right_column.markdown(styled_text, unsafe_allow_html=True)

    # "More About Me" text aligned in the center

    a_text = """
        <style>
            .about-container {
                max-width: 800px;
                margin: 0 auto;
                padding-top: 100px;
                padding-bottom: 50px;
                text-align: justify;
                font-size: 20px;
                line-height: 1.6;
                color: #ffffff;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            .about-heading {
                font-size: 36px;
                font-weight: bold;
                text-align: left;
                margin:auto;
                color: #00ff99;
                margin-bottom: 50px;
                font-family: "Arial Black", sans-serif;
            }
            .about-text {
                padding-bottom: 70px;
            }
            .highlight {
                background: linear-gradient(45deg, #ff5f6d, #ff9970);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: bold;
            }
        </style>
        <div class="about-container">
            <h1 class="about-heading">About me:</h1>
            <div class="about-text">
                <p>
                    I am a highly skilled professional with expertise in multiple domains, making me a versatile asset capable of tackling diverse challenges.
                    As an <span class="highlight">UiPath RPA developer</span>, I specialize in creating efficient automation solutions that streamline business processes and boost productivity.
                    My proficiency as an <span class="highlight">ML engineer</span> allows me to leverage advanced algorithms to build intelligent systems that extract valuable insights from data.
                </p>
                <p>
                    In addition to <span class="highlight">RPA and ML</span>, I possess a strong background in <span class="highlight">data analysis</span>.
                    Using SQL and Power BI, I delve deep into datasets, uncovering meaningful patterns and trends to drive data-driven decisions.
                    My ability to work with Power BI allows me to create interactive and visually compelling dashboards, presenting complex information in an accessible and understandable manner.
                </p>
                <p>
                    With my combined expertise in <span class="highlight">RPA, ML, and data analysis</span>, I am equipped to solve complex problems and optimize processes for businesses.
                    My passion for staying at the forefront of technological advancements ensures that I can deliver innovative and effective solutions that drive growth and success.
                    As a diligent professional, I am dedicated to making a significant impact on projects and contributing to the overall success of any organization.
                </p>
            </div>
        </div>
    """

    st.markdown(a_text, unsafe_allow_html=True)

       #my service section::
    
    

    st.markdown("<h1 style='text-align:justify;color:#00ff99; margin:auto;padding-top:150px;'>What I do:</h1>", unsafe_allow_html=True)


    st.markdown(
        """
        <style>
        .service-item {
            background-color: black;
            margin: 80px;
            padding: 10px;
            width : 260px;
            box-shadow: 5 2px 4px rgba(5000, 0, 0, 0.1);
            border-radius: 40px;
            overflow: hidden;
            transition: transform 0.3s;
            margin-bottom: 200px; /* Add spacing between rows */
        }
        .book-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2);
        }
        .service-image {
            height: 70px;
            
            border-top-left-radius: 70px;
            border-top-right-radius: 10px;
            margin: auto;
        }
        
        .title {
            font-size: 20px;
            font-weight: bold;
            color: #FFFFFF;
            margin-left: 50px;
            margin-bottom: 5px;
        }
        
        .custom-button {
        background-color: #4CAF50; /* Green background */
        border: none; /* Remove border */
        color: white; /* White text color */
        padding: 10px 20px; /* Add padding */
        text-align: center; /* Center-align text */
        text-decoration: none; /* Remove underline */
        display: inline-block; /* Make it inline */
        font-size: 16px; /* Set font size */
        border-radius: 5px; /* Add border radius */
        cursor: pointer; /* Add cursor pointer on hover */
        margin-top: 10px; /* Add top margin */
    }
    .custom-button:hover {
        background-color: #45a049; /* Dark green on hover */
    }
        </style>
        """,
        unsafe_allow_html=True
    )


    services_data_dict = [
        {
            "image_url": "https://ravh-it.com/wp-content/uploads/2020/07/data-science-logo-icon.png",
            "title":"Data Science",
            "content": "In the realm of Data Science and Machine Learning, I uncover the hidden potential within your data using sophisticated algorithms. Elevate your business with insights that drive informed decisions and streamlined processes. Embrace the forefront of innovation with cutting-edge Machine Learning techniques. Let's collaborate to achieve shared success on this transformative journey!",
        },
         {
            "image_url": "https://assets.datacamp.com/production/tracks/1206/badges/original/Data_Analyst.png?1558088045",
            "title": "Data Analysis",
            "content": "From data modeling to interactive dashboards, I offer tailored solutions for optimizing your business strategies. Embrace the power of data-driven decision-making and drive growth with my expertise in Data Analysis and Power BI. Let's explore the potential of your data together!",
        },
        {
            "image_url":("https://synapticap.com/wp-content/uploads/2020/10/ui-path-logo-1.png"),
             "title":"Robotic process Automation",
            "content": "As an RPA specialist, I automate repetitive tasks, boost productivity, and integrate RPA solutions into your existing systems. Embrace efficiency and innovation for your business success. Let's work together to unleash the power of automation.",

        },
        
       
    ]

    row = st.columns(4)
    for i in range(len(services_data_dict)):
        with row[i % 4]:

            st.markdown(
                f"""
                <div class="service-item">
                    <img class="service-image" src="{services_data_dict[i]['image_url']}">
                    <h2 class="title">{services_data_dict[i]['title']}</h2>  <!-- Use h2 instead of p for the title -->
                    <p class="content">{services_data_dict[i]['content']}</p>
                     

                </a>
                </div>
                """,
                unsafe_allow_html=True
            )
    st.markdown("<h1 style='text-align: left;padding-top:50px;padding-bottom:100px ;color:#00ff99; margin :auto;' >My Skills:</h1>", unsafe_allow_html=True)
    technical, Professional_column = st.columns(2)

    technical.markdown("<h3 style='text-align: left;padding-top:40px;margin-left:10px;text-decoration: underline;' >Technicals Skills:</h3>", unsafe_allow_html=True)

    technical_skills = [
        {"skill": "UIpath RPA", "level": 95},
        {"skill": "Machine Learning", "level": 80},
        {"skill": "statistics & Mathematics", "level": 70},
        {"skill": "Automation Solution Architech", "level": 70},
        {"skill": "python", "level": 80},
        {"skill": "Html &css", "level": 70},
        {"skill": "Power BI", "level": 80},
        {"skill": "Deep learning", "level": 70},
        # Add more skills as needed
    ]
    skill_colors = {
        "UIpath RPA": "#FF5733",
        "Machine Learning": "#33FF57",
        "statistics & Mathematics": "#5733FF",
        "Automation Solution Architech": "#FF33E1",
        "python": "#FF5733",
        "Html &css": "#33FF57",
        "Power BI": "#5733FF",
        "Deep learning": "#FF33E1",
    }
    skill_icons = {
        "UIpath RPA": "robot",
        "Machine Learning": "cogs",
        "statistics & Mathematics": "chart-bar",
        "Automation Solution Architech": "laptop-code",
        "python": "python",
        "Html &css": "code",
        "Power BI": "chart-pie",
        "Deep learning": "brain",
    }

    for skill_info in technical_skills:
        skill = skill_info["skill"]
        level = skill_info["level"]

        skill_color = skill_colors.get(skill,
                                       "#4CAF50")  # Use a default color (#4CAF50) if the skill is not found in the dictionary
        icon_name = skill_icons.get(skill, "question")
        technical.markdown(f"<h6><i class='fas fa-{icon_name}'></i> {skill}</h6>", unsafe_allow_html=True)
        progress_width = level * 3  # Adjust the multiplier to control the size
        glow_effect = f"box-shadow: 0 0 2px {skill_color}, 0 0 2px {skill_color}, 0 0 8px {skill_color};"

        css_animation = f"""
                @keyframes fillup {{
                    0% {{ width: 0; }}
                    100% {{ width: {level}% }}
                }}
            """

        # Apply the animation to the progress bar
        progress_bar = f"""
                <style>
                    {css_animation}
                </style>
                <div style="background-color: #ddd; border-radius: 3px; width: 300px; height: 5px; {glow_effect}">
                    <div style="background-color: {skill_color}; width: {level}%; height: 100%; border-radius: 3px; animation: fillup 10s linear;">
                    </div>
                </div>
            """
        technical.markdown(progress_bar, unsafe_allow_html=True)
    st.markdown("<p style='margin-top: 230px;'>Navigate to <span style='color: yellow;'>My Projects</span> and <span style='color: yellow;'>Resume</span> on the left side</p>", unsafe_allow_html=True)





    Professional_column.markdown("<h3 style='text-align: left;padding-top:40px;margin-left:10px;text-decoration: underline;' >Professionals Skills:</h3>", unsafe_allow_html=True)

    profession_skills1 = [
        {"skill": "TeamWork", "level": 90},
        {"skill": "communication", "level": 80},

    ]
    profession_skills2 = [
        {"skill": "Problem Solving", "level": 85},
        {"skill": "Project Management", "level": 80},
    ]

    # Display  profession skills with circular progress bars

    Pcol1, Pcol2 = Professional_column.columns(2)

    for skill_info in profession_skills1:
        skill = skill_info["skill"]
        level = skill_info["level"]

        radius = 45
        circumference = 2 * 3.14 * radius
        progress = (100 - level) * circumference / 100


        colors = ["#2196F3", "#9C27B0", "#2196F3", "#9C27B0"]

        color_index = profession_skills1.index(skill_info) % len(colors)
        skill_color = colors[color_index]

        Pcol1.markdown(f"<h6 style='color: {skill_color};padding-top:10px;'>{skill}</h6>", unsafe_allow_html=True)

        circular_progress_bar = f"""
            <svg width="90" height="100" viewBox="0 0 100 100" style="filter: drop-shadow(0 0 5px rgba(0, 255, 0, 0.4));">
                <circle cx="50" cy="50" r="{radius}" fill="transparent" stroke="#ddd" stroke-width="10"></circle>
                <circle cx="50" cy="50" r="{radius}" fill="transparent" stroke="{skill_color}" stroke-width="10"
                        stroke-dasharray="{circumference}" stroke-dashoffset="{progress}"></circle>
                <text x="50" y="50" text-anchor="middle" fill="{skill_color}" font-size="18" dy="6">{level}%</text>
            </svg>
        """
        Pcol1.markdown(circular_progress_bar, unsafe_allow_html=True)


    for skill_info in profession_skills2:
            skill = skill_info["skill"]
            level = skill_info["level"]


            radius = 45
            circumference = 2 * 3.14 * radius
            progress = (100 - level) * circumference / 100

            colors = ["#FF0000", "#FFFF00"]

            color_index = profession_skills2.index(skill_info) % len(colors)
            skill_color = colors[color_index]

            Pcol2.markdown(f"<h6 style='color: {skill_color};padding-top:10px;'>{skill}</h6>", unsafe_allow_html=True)

            circular_progress_bar = f"""
                        <svg width="90" height="100" viewBox="0 0 100 100" style="filter: drop-shadow(0 0 4px rgba(0, 255, 0, 0.5));">
                            <circle cx="50" cy="50" r="{radius}" fill="transparent" stroke="#ddd" stroke-width="10"></circle>
                            <circle cx="50" cy="50" r="{radius}" fill="transparent" stroke="{skill_color}" stroke-width="10"
                                    stroke-dasharray="{circumference}" stroke-dashoffset="{progress}"></circle>
                            <text x="50" y="50" text-anchor="middle" fill="{skill_color}" font-size="18" dy="6">{level}%</text>
                        </svg>
                    """
            Pcol2.markdown(circular_progress_bar, unsafe_allow_html=True)



def show_projects_page():
    # st.header("Projects")

    category = st.sidebar.radio("Select a category:", ( "Data Science-ML Projects","RPA Projects"))

    st.markdown(
        """
        <style>
        .service-item {
            background-color: black;
            margin: 80px;
            padding: 10px;
            width : 400px;
            box-shadow: 5 2px 4px rgba(5000, 0, 0, 0.1);
            border-radius: 40px;
            overflow: hidden;
            transition: transform 0.3s;
            margin-bottom: 80px; /* Add spacing between rows */
        }
        .book-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2);
        }
        .service-image {
            height: 350px;
            width:350px
            border-top-left-radius: 200px;
            border-top-right-radius: 200px;
            margin: auto;
        }
        .book-details {
            padding: 10px;
            text-align: center;
        }
        .title {
            font-size: 20px;
            font-weight: bold;
            color: #FFFFFF;
            margin-left: 50px;
            margin-bottom: 5px;
        }

        .custom-button {
        background-color: black; /* Green background */
        width:300px;
        border: 2px solid white; /* Remove border */
        color: white; /* White text color */
        padding-top: 5px; /* Add padding */
        text-align: center; /* Center-align text */
        text-decoration: none; /* Remove underline */
        display: inline-block; /* Make it inline */
        font-size: 20px; /* Set font size */
        border-radius: 20px; /* Add border radius */
        cursor: pointer; /* Add cursor pointer on hover */
        margin-left: 50px;
        margin-top: 10px; /* Add top margin */
    }
    .custom-button:hover {
        background-color: #808080; /* Dark green on hover */
    }
    @media (max-width:700px){
        .service-item{
            width:90%;
            margin:40px auto
        }
    }
        </style>
        """,
        unsafe_allow_html=True
    )


    if category == "RPA Projects":
             st.title("Robotics Process Automation Projects")
             RPA_dict = [

                 {
                     "image_url": "https://akabot.com/wp-content/uploads/2021/06/b2-1.png",
                     "title": "Buisnesses Invoices Generator",
                     "content": "This avant-garde project automates invoice generation for large businesses. It seamlessly integrates with databases, third-party apps, and email systems to swiftly create and distribute invoices. Boosting efficiency and accuracy, it sets new standards for streamlined business operations.",
                     "project_link": "https://github.com/iamanimesh11/rpaproject_invoice_generator",
                     "document-link": "https://github.com/iamanimesh11/rpaproject_invoice_generator/blob/main/Data/buisness%20files/pdd%20document.pdf"

                 },

                 {
                     "image_url": "https://th.bing.com/th/id/OIP.WatBDJy77PD3IJEpH5CFAAAAAA?pid=ImgDet&w=370&h=370&rs=1",
                     "title": "Finance-Loan-Application-Processor",
                     "content": "The Finance Loan Application Process Project is a cutting-edge system that automates loan applications. Extracting data from Excel, it seamlessly populates the loan site and handles complex exceptions. Adapting to loan criteria, it ensures an efficient and reliable application process, setting new standards for the financial industry.",
                     "project_link": "https://github.com/iamanimesh11/finance-Loan-Application-process-project",
                     "document-link": "https://github.com/iamanimesh11/finance-Loan-Application-process-project/blob/main/Data/PDD_Loan%20Application%20Processing.pdf"

                 },
                 {
                     "image_url": (
                         "https://margmultisolutions.com/wp-content/uploads/2021/07/e-invoicing-software.png"),
                     "title": "Buisnesses Invoices Processor",
                     "content": " This cutting-edge project streamlines large enterprise operations, automating client data management. It retrieves Invoice emails, downloads attachments, and extracts data using advanced OCR technology. Organized reports are promptly sent to designated recipients, revolutionizing invoicing efficiency and data handling.",
                     "project_link": "https://github.com/iamanimesh11/project_invoice_processing",
                     "document-link": "https://github.com/iamanimesh11/project_invoice_processing/blob/main/Data/process%20design%20document.pdf"
                 },
                 {
                     "image_url": (
                         "https://th.bing.com/th/id/OIP.Xu4cvMthf6lV0UxzYI1V3QHaHa?w=171&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7"),
                     "title": "Advanced yearly Reports generator",
                     "content": " Utilizing UiPath Studio and Orchestrator, it employs the advanced REFramework template to collect, process, and create final yearly reports, while seamlessly updating statuses with unique identifiers. This project equips learners to tackle complex automation challenges with finesse.",
                     "project_link": "https://github.com/iamanimesh11/project_generate_yearly_report",
                     "document-link": "https://github.com/iamanimesh11/project_generate_yearly_report"
                 },
             ]

             row = st.columns(2)
             for i in range(len(RPA_dict)):
                 with row[i % 2]:

                     st.markdown(
                         f"""
                                 <div class="service-item">
                                     <img class="service-image" src="{RPA_dict[i]['image_url']}">
                                     <h2 class="title">{RPA_dict[i]['title']}</h2>  <!-- Use h2 instead of p for the title -->
                                     <p class="content">{RPA_dict[i]['content']}</p>
                                     <a href="{RPA_dict[i]['project_link']}" target="_blank">
                                      <button class="custom-button">Project Files</button>
                                      </a>
                                      <a href="{RPA_dict[i]['document-link']}" target="_blank">
                                      <button class="custom-button">Process design Document</button>
                                      </a>
                                 </div>
                                 """,
                         unsafe_allow_html=True
                     )



    elif category == "Data Science-ML Projects":
        st.title("My Machine and Deep learning Projects")
        ml_dict = [

            {
                "image_url": "https://th.bing.com/th/id/R.a327e023722b4506d47109f5c1195c4f?rik=0WJP2n5DlncuAQ&riu=http%3a%2f%2ffreedesignfile.com%2fupload%2f2015%2f10%2fCinema-movie-vector-background-graphics-08.jpg&ehk=3hacHgfJZ3s%2bfWrc3ALOjEgZZNznMDCi2QEnT0%2fuR2w%3d&risl=&pid=ImgRaw&r=0",
                "title": "Movies Suggestion Engine",
                "content": "With a vast database of movies and a powerful recommendation algorithm, Movie Suggest helps you discover your next favorite films effortlessly.app generates personalized movie recommendations based on your favorite films. Simply type in the name of a movie you love, and Movie Suggest will present you with a handpicked list of similar movies that are sure to pique your interest.",
                "project_link": "https://cinemanexus.streamlit.app/",
                "document-link": "https://github.com/iamanimesh11/cinema_nexus"

            },

            {
                "image_url": "https://th.bing.com/th/id/OIP.89POGV1TEhd2vmqY6YtjPQHaE8?pid=ImgDet&rs=1",
                "title": "Books Explorer Engine",
                "content": "Uncover your next favorite book effortlessly with our Intelligent Book Suggester web app. Utilizing advanced collaborative filtering techniques and state-of-the-art machine learning algorithms, it offers highly accurate top-rated book recommendations tailored specifically to your unique preferences.Say goodbye to endless searching and let our web app take the guesswork out of finding your next literary adventure  ",
                "project_link": "https://intelligencebookssuggesterapp.streamlit.app/",
                "document-link": "https://github.com/iamanimesh11/intelligence_books_suggester_App"

            },
            {
                "image_url": "https://th.bing.com/th/id/OIP.TxTL77s6_nJbxM6mME4ScAHaDx?pid=ImgDet&w=783&h=399&rs=1",
                "title": "Spam Buster AI -an msg spam classifier ml",
                "content": "Detect spam messages instantly and stay safe from harmful content. Input your message via text or upload a file. The app will provide a verdict on spam presence and raise a red alert if necessary. Explore the word cloud to see frequent spam-related words. Enjoy the interactive experience and learn about spam classification with this educational app!",
                "project_link": "https://spambusterai.streamlit.app/",
                "document-link": "https://github.com/iamanimesh11/SpamBuster_AI"

            },
        ]

        row = st.columns(2)
        for i in range(len(ml_dict)):
            with row[i % 2]:

                st.markdown(
                    f"""
                                         <div class="service-item">
                                             <img class="service-image" src="{ml_dict[i]['image_url']}">
                                             <h2 class="title">{ml_dict[i]['title']}</h2>  <!-- Use h2 instead of p for the title -->
                                             <p class="content">{ml_dict[i]['content']}</p>
                                             <a href="{ml_dict[i]['project_link']}" target="_blank">
                                              <button class="custom-button">Check out website</button>
                                              </a>
                                              <a href="{ml_dict[i]['document-link']}" target="_blank">
                                              <button class="custom-button">Projects Files</button>
                                              </a>
                                         </div>
                                         """,
                    unsafe_allow_html=True
                )


    # elif category == "Data Analytics Projects":
    #          st.title("My Data Analytics  Projects")
    #          ml_dict = [

    #              {
    #                  "image_url": "https://uktechnews.co.uk/wp-content/uploads/2021/10/shutterstock_1458463553-scaled.jpg",
    #                  "title": "Sales Intelligence Console PowerBI",
    #                  "content": "The Sales Analysis Dashboard provides an intuitive and interactive interface, enabling you to explore key performance indicators (KPIs) and sales metrics in real-time.Gain real-time insights, track sales performance, and identify growth opportunities effortlessly. Make data-driven decisions and stay ahead in today's dynamic business landscape",
    #                  "project_link": "https://github.com/iamanimesh11/sales_intelligence_console_powerBi/blob/main/sales%20console_myDocument.pdf",
    #                  "document-link": "https://github.com/iamanimesh11/sales_intelligence_console_powerBi"

    #              },



    #          ]

    #          row = st.columns(2)
    #          for i in range(len(ml_dict)):
    #              with row[i % 2]:

    #                  st.markdown(
    #                      f"""
    #                                                   <div class="service-item">
    #                                                       <img class="service-image" src="{ml_dict[i]['image_url']}">
    #                                                       <h2 class="title">{ml_dict[i]['title']}</h2>  <!-- Use h2 instead of p for the title -->
    #                                                       <p class="content">{ml_dict[i]['content']}</p>
    #                                                       <a href="{ml_dict[i]['project_link']}" target="_blank">
    #                                                        <button class="custom-button">Analysis Report</button>
    #                                                        </a>
    #                                                        <a href="{ml_dict[i]['document-link']}" target="_blank">
    #                                                        <button class="custom-button">Projects Files</button>
    #                                                        </a>
    #                                                   </div>
    #                                                   """,
    #                      unsafe_allow_html=True
    #                  )


def show_resume_page():

    from pathlib import Path

    import streamlit as st
    from PIL import Image

    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir / "main.css"
    resume_file = current_dir / "animesh_Resume.pdf"
    profile_pic = current_dir / "unnamed-removebg-preview-modified.png"

    PAGE_TITLE = "Digital CV | Animes Singh"
    PAGE_ICON = ":wave:"
    NAME = "Animesh Singh"
    DESCRIPTION = """
    Data Analyst, Ml engineer and RPA developer.
    """
    EMAIL = "iamanimesh11june@gmail.com"
    SOCIAL_MEDIA = {
        "LinkedIn": "https://www.linkedin.com/in/animesh-singh11/",
        "GitHub": "https://github.com/iamanimesh11",
        "Website": "",
    }
    PROJECTS = {
        "🏆 intelligent Sales console -visuals for sales forecasting ": "https://github.com/iamanimesh11/sales_intelligence_console_powerBi",
        "🏆 Buisnesses Invoices Generator -process to automate invoice generation for business": "",
        "🏆 Finance-Loan-Application-Processor-Business process  to automoate loan applicatons error free": "",
        "🏆 Buisnesses Invoices Processor- process to extract clients data  using advanced OCR tech": "",
        "🏆 Advanced yearly Reports generator-: Automates the creation of comprehensive annual reports": "",
        "🏆 Movie suggestion Engine -: Offers personalized recommendations based on user movie preferences, ": "",
        "🏆 Books suggestion Engine -: Employs priority-based and collaborative filtering algorithms to provide personalized book recommendations, ": "",


    }

    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

    # col1, col2 = st.columns(2, gap="small")
    col1, col2 = st.columns([1,3])
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)

    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
        
    st.container()
    st.write('\n')
    st.subheader("Education & Qulifications")
    st.write(
        """
    - ✔️ Bachleor of technology in computer science engineering 
    - ✔️ Proficient in RPA development, utilizing automation tools to streamline processes and improve efficiency.
    - ✔️ Good understanding of statistical mathematics for machine leaning
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """
    )

    # --- SKILLS ---
    st.container()
    st.write('\n')
    st.subheader(" Skills")
    st.write(
        """
    - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL,.net,HTML/CSS
    - 🤖 Automation -UiPath soltuion architect
    - 📊 Data Visulization: PowerBi, MS Excel, Plotly
    - 📚 ml,dl:pytorch ,keras,CNN,NLP,Model Deployment
    - 🗄️ Database: MySQL
    """
    )
    st.container()
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

    st.write("🚧", "**Virual internship - Data Analyst |Lagazon Tech")
    st.write("07/2023 - Present")
    st.write(
        """
    - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
    - ►implemented powerbi visuals in real life projects 
    """
    )

    st.write('\n')
    st.write("🚧", "RPA automation and develoment |AICTE EduSkills UiPath")
    st.write("05/2023 - 07/2023")
    st.write(
        """
    - ► Build real world Automation workflows with handling all exceptions that may occur
    - ► designed and built custom workflows and automation scripts to streamline repetitive tasks, allowing employees to focus on more strategic activities.
    - ►  learned to troubleshoot and optimize automation workflows, ensuring smooth and error-free execution.
    """
    )
    st.container()
    st.write('\n')
    st.subheader("Projects :")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")









def image_to_base64(image):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()


if __name__ == "__main__":
    main()
