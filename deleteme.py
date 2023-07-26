import streamlit as st
import time
from PIL import Image
import os


def main():
    st.set_page_config(page_title="My Streamlit App", page_icon=":smiley:", layout="wide",
                       initial_sidebar_state="expanded")

    # Sidebar navigation panel
    st.sidebar.title("Navigation")
    navigation_options = ["Home", "Projects", "Resume"]
    selected_option = st.sidebar.selectbox("Go to", navigation_options)

    # Display content based on selected option
    if selected_option == "Home":
        show_home_page()
    elif selected_option == "Projects":
        show_projects_page()
    elif selected_option == "Resume":
        show_resume_page()


def show_home_page():
    page_bg_img = '''
    <style>
    body {
      background-image: linear-gradient(to bottom, #000000, #ffffff);
      background-attachment: fixed;
    }
    </style>
    '''

    # Apply the background image style using st.markdown
    st.markdown(page_bg_img, unsafe_allow_html=True)

    left_column, right_column = st.columns(2)
    # Beautify the image with CSS styles
    image = Image.open("unnamed-removebg-preview-modified.png")
    image_html = f"<img src='data:image/png;base64,{image_to_base64(image)}' " \
                 f"style='border: 2px solid #ffffff; border-radius: 160px; box-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 40px #00ff00;' " \
                 f"width='300' alt='Beautiful Image'>"


    left_column.markdown(image_html, unsafe_allow_html=True)
    # glowing_text_css = get_glowing_text_css()
    # st.markdown(glowing_text_css, unsafe_allow_html=True)
    styled_text = """
               <style>
                .underlined-text {
                    font-size: 30px;
                    border-bottom: 3px solid white;
                    display : online;
                    padding-bottom: 5px;
                    font-family: "Times New Roman", Times, serif;
                }
               </style>
               <div style='text-align: center;padding-bottom: 100px;'>
                   <h4 style='color: #ffffff;text-align: left;padding-bottom: 0px; margin: 0;'>
                       Hello, I am
                   </h4>
                   <h1 style='color: #ffffff;text-align: left; font-weight: bold; margin: 0;'>
                       Animesh Singh
                   </h1>
                   <h4 style='color: #ffffff;text-align: left; padding-top: 0px; margin: 0;'>
                       And I'm a  <p style='color: green; font-size:30px; font-weight: bold; margin: 0;'>
                      <span class="underlined-text glowing-text" id='role'> <!-- Added 'glowing-text' class here -->
                              RPA Developer, ML Developer, Data Analyst
                    </span>
                   </p>
                   </h4>

               </div>
           """
    right_column.markdown(styled_text, unsafe_allow_html=True)

    # "More About Me" text aligned in the center
    st.text("")
    st.markdown("<h1 style='text-align: left;margin-left:400px; padding-top:250px; padding-bottom:50px'>About me:</h1>",
                unsafe_allow_html=True)
    about_text = """

                <div padding-bottom:70px>
                    <p style="font-size: 20px; padding-bottom:70px line-height: 1.6; color: #ffffff;"> 
                    I am a highly skilled professional with expertise in multiple domains, making me a versatile asset capable of tackling diverse challenges. As an UiPath RPA developer, I specialize in creating efficient automation solutions that streamline business processes and boost productivity. My proficiency as an ML engineer allows me to leverage advanced algorithms to build intelligent systems that extract valuable insights from data.
                    In addition to RPA and ML, I possess a strong background in data analysis. Using SQL and Power BI, I delve deep into datasets, uncovering meaningful patterns and trends to drive data-driven decisions. My ability to work with Power BI allows me to create interactive and visually compelling dashboards, presenting complex information in an accessible and understandable manner.
                    With my combined expertise in RPA, ML, and data analysis, I am equipped to solve complex problems and optimize processes for businesses. My passion for staying at the forefront of technological advancements ensures that I can deliver innovative and effective solutions that drive growth and success. As a diligent professional, I am dedicated to making a significant impact on projects and contributing to the overall success of any organization.</p>
                </div>
         """
    st.markdown(about_text, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:left; margin-left:350px;padding-top:150px;'>My Services:</h1>",
                unsafe_allow_html=True)
    #  col1, col2, col3 = st.columns(3)

    # # CSS style for the service box with glow effect
    # service_box_style = """
    #             border: 2px solid #cccccc;
    #             border-radius: 50px;
    #             padding: 20px;
    #             height: 300px;
    #             flex-direction: column;
    #             justify-content: center;
    #             word-wrap: break-word;
    #             box-shadow: 0 0 10px #00ff00, 0 0 5px #00ff00, 0 0 5px #00ff00, 0 0 5px #00ff00;
    #             animation: glow 2s ease-in-out infinite;
    #         """
    #
    # with col1:
    #     st.markdown("<div style='" + service_box_style + "'>gubhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioububobuuuuuuuuuuuuuuuuuuuvyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy </div>", unsafe_allow_html=True)
    #     st.image("unnamed-removebg-preview-modified.png", width=100)
    #     # st.markdown("</div>", unsafe_allow_html=True)
    #
    #
    #
    # with col2:
    #     st.markdown("<div style='" + service_box_style + "'>Content for Service 2</div>", unsafe_allow_html=True)
    #     st.markdown("</div>", unsafe_allow_html=True)
    #
    # # Service 3 with glow effect
    # with col3:
    #     st.markdown("<div style='" + service_box_style + "'>Content for Service 2</div>", unsafe_allow_html=True)
    #     st.markdown("</div>", unsafe_allow_html=True)
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
            "image_url": ("https://synapticap.com/wp-content/uploads/2020/10/ui-path-logo-1.png"),
            "title": "Robotic process Automation",
            "content": "As an RPA specialist, I automate repetitive tasks, boost productivity, and integrate RPA solutions into your existing systems. Embrace efficiency and innovation for your business success. Let's work together to unleash the power of automation.",
            # "button_link": "https://example.com/item1",
        },
        {
            "image_url": "https://i.pinimg.com/originals/6f/d8/3f/6fd83f6c101f85bb417448302daedfb9.png",
            "title": "Machine Learning",
            "content": "As a Machine Learning expert, I unlock the power of data through advanced algorithms. Empower your business with data-driven decisions and optimized processes. Embrace the future of innovation with Machine Learning. Let's achieve success together! Let's embark on this transformative journey together!",
            # "button_link": "https://example.com/item2",
        },
        {
            "image_url": "https://assets.datacamp.com/production/tracks/1206/badges/original/Data_Analyst.png?1558088045",
            "title": "Data Analysis",
            "content": "From data modeling to interactive dashboards, I offer tailored solutions for optimizing your business strategies. Embrace the power of data-driven decision-making and drive growth with my expertise in Data Analysis and Power BI. Let's explore the potential of your data together!",
        },
        # Add more items as needed
    ]
    button_label = "My Projects"
    projects_page_url = "/Resume"
    row = st.columns(4)
    for i in range(len(services_data_dict)):
        with row[i % 4]:  # Use row[i % 4] to create 4 columns

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
    st.markdown(
        "<h1 style='text-align: left;padding-top:50px;padding-bottom:100px ; margin-left:320px' >My Skills:</h1>",
        unsafe_allow_html=True)
    technical, Professional_column = st.columns(2)

    technical.markdown(
        "<h3 style='text-align: left;padding-top:40px;margin-left:10px;text-decoration: underline;' >Technicals Skills:</h3>",
        unsafe_allow_html=True)

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
    for skill_info in technical_skills:
        skill = skill_info["skill"]
        level = skill_info["level"]

        technical.markdown(f"<h6>{skill}</h3>", unsafe_allow_html=True)
        progress_width = level * 3  # Adjust the multiplier to control the size
        glow_effect = "box-shadow: 0 0 2px #00ff00, 0 0 5px #00ff00, 0 0 10px #00ff00;"

        # Display the custom progress bar
        progress_bar = f"""
                <div style="background-color: #ddd; border-radius: 3px; width: 300px; height: 5px; {glow_effect}">
                    <div style="background-color: #4CAF50; width: {progress_width}px; height: 100%; border-radius: 3px;">
                    </div>
                </div>
                """
        technical.markdown(progress_bar, unsafe_allow_html=True)

    Professional_column.markdown(
        "<h3 style='text-align: left;padding-top:40px;margin-left:10px;text-decoration: underline;' >Professionals Skills:</h3>",
        unsafe_allow_html=True)

    profession_skills1 = [
        {"skill": "TeamWork", "level": 90},
        {"skill": "communication", "level": 80},

    ]
    profession_skills2 = [
        {"skill": "Problem Solving", "level": 85},
        {"skill": "Project Management", "level": 80},
    ]

    # Display your profession skills with circular progress bars

    Pcol1, Pcol2 = Professional_column.columns(2)

    for skill_info in profession_skills1:
        skill = skill_info["skill"]
        level = skill_info["level"]

        radius = 45
        circumference = 2 * 3.14 * radius
        progress = (100 - level) * circumference / 100
        Pcol1.markdown(f"<h6>{skill}</h6>", unsafe_allow_html=True)

        circular_progress_bar = f"""
                   <svg width="90" height="100" viewBox="0 0 100 100" style="filter: drop-shadow(0 0 7px rgba(0, 255, 0, 0.8));">
        <circle cx="50" cy="50" r="{radius}" fill="transparent" stroke="#ddd" stroke-width="10"></circle>
        <circle cx="50" cy="50" r="{radius}" fill="transparent" stroke="#4CAF50" stroke-width="10"
                stroke-dasharray="{circumference}" stroke-dashoffset="{progress}"></circle>
        <text x="50" y="50" text-anchor="middle" fill="#4CAF50" font-size="18" dy="6">{level}%</text>
    </svg>
    """
        Pcol1.markdown(circular_progress_bar, unsafe_allow_html=True)

    for skill_info in profession_skills2:
        skill = skill_info["skill"]
        level = skill_info["level"]

        radius = 45
        circumference = 2 * 3.14 * radius
        progress = (100 - level) * circumference / 100
        Pcol2.markdown(f"<h6>{skill}</h6>", unsafe_allow_html=True)

        circular_progress_bar = f"""
                       <svg width="90" height="100" viewBox="0 0 100 100" style="filter: drop-shadow(0 0 7px rgba(0, 255, 0, 0.8));">
        <circle cx="50" cy="50" r="{radius}" fill="transparent" stroke="#ddd" stroke-width="10"></circle>
        <circle cx="50" cy="50" r="{radius}" fill="transparent" stroke="#4CAF50" stroke-width="10"
                stroke-dasharray="{circumference}" stroke-dashoffset="{progress}"></circle>
        <text x="50" y="50" text-anchor="middle" fill="#4CAF50" font-size="18" dy="6">{level}%</text>
    </svg>
    """
        Pcol2.markdown(circular_progress_bar, unsafe_allow_html=True)

def show_projects_page():
     st.header("Projects")

        # def rpa_projects():
        #   st.subheader("RPA Projects")
        #   st.write("Description of RPA project 1.")
        #   st.write("Description of RPA project 2.")

    # Sidebar category selection
    category = st.sidebar.radio("Select a category:",
                                ("RPA Projects", "Machine Learning Projects", "Data Analytics Projects"))

    # Display content based on selected category


     if category == "RPA Projects":
    rpa_projects()

    elif category == "Machine Learning Projects":
        st.subheader("Machine Learning Projects")
        st.write("Description of ML project 1.")
        st.write("Description of ML project 2.")
    elif category == "Data Analytics Projects":
        st.subheader("Data Analytics Projects")
        st.write("Description of data analytics project 1.")
        st.write("Description of data analytics project 2.")

def show_resume_page():
    st.header("Resume")
    # Add your resume content here


def image_to_base64(image):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()



if __name__ == "__main__":
    main()
