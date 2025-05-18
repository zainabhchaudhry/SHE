SHE - Women-Only Ride-Hailing App
🚗 Safe. Secure. SHE.

Vision
SHE is a pioneering ride-hailing platform created to empower women by providing a safe, secure, and comfortable commuting experience. Driven by women, for women, SHE aims to revolutionize the ride-hailing industry by focusing on safety, trust, and community empowerment.

Our mission is to foster an inclusive environment where women feel secure while traveling and where female drivers can generate sustainable income within a supportive ecosystem. SHE is not just a ride-hailing app; it’s a movement to make transportation safer and more accessible for women.

Business Idea & Revenue Model
Revenue Streams:
Ride Commissions:

A small percentage fee is charged on every completed ride to sustain the platform.

Subscription Plans:

Premium memberships offering discounts, priority rides, and additional safety features.

Advertising & Partnerships:

Collaborations with women-centric brands and services within the app.

In-app promotions targeting the female demographic.

User Acquisition & Marketing:
Targeted social media campaigns emphasizing women’s safety and community empowerment.

Partnerships with women’s organizations, educational institutions, and workplaces.

Referral programs that incentivize users to bring in new riders and drivers.

Brand Identity:
Brand Name: SHE

Tagline: “Safe. Secure. SHE.”

Visual Identity:

Logo and website (planned) reflecting empowerment, safety, and community.

Community Engagement:

Building a strong online presence through social media and local community events.

How This App Aligns with the Winning Criteria
Criteria	Description
Code Functionality & Best Practices	The app follows modular programming principles using Python functions. Streamlit session states manage navigation, while error handling ensures robustness. The UI is clean, intuitive, and responsive.
Business Viability	Addresses a real-world problem—women’s safety in transportation. The multi-revenue approach, including ride commissions, subscriptions, and ads, ensures scalability and financial sustainability.
User Experience	Intuitive navigation with clear page transitions (Landing, Authentication, Home, Map). Lottie animations and informative messages enhance engagement. The UI is user-friendly and visually appealing.
Creativity & Usefulness	A unique focus on women-only ride-hailing, prioritizing safety and community support. Future plans include real-time tracking, comprehensive driver-rider profiles, and interactive dashboards.

Features Implemented
Landing Page:
Animated introduction using Lottie files, highlighting the purpose of SHE.

Welcome message with a clear call-to-action to get started.

User Authentication:
Simple login system using dummy credentials for demonstration.

Secure login process with feedback for both success and failure cases.

Redirects to the Map page upon successful login.

Page Navigation:
Utilizes Streamlit session states for smooth page transitions.

Mimics a Single Page Application (SPA) feel within Streamlit.

Engaging Animations & Visuals:
Integrates Lottie animations for a modern and interactive experience.

Custom banner images with captions to reinforce the brand message.

Safety & Community Focus:
Clearly conveys the mission of providing a secure and empowering ride-hailing experience.

Supports future expansion into real-time safety features and community building.

Planned Future Enhancements:
Authentication:

Integrate with secure databases for real user management.

Payment Gateway:

Integrate with Stripe to handle ride payments and subscription processing.

Real-Time Ride Tracking:

Map page integration with live GPS tracking for drivers and riders.

Driver & Rider Profiles:

Comprehensive profiles with ride history and feedback system.

Admin Dashboard:

Ride analytics and user management for better platform control.

Marketing Website:

Develop a dedicated website with SEO for user acquisition.

How to Run the App:
1. Install Dependencies:
bash
Copy
Edit
pip install streamlit streamlit-lottie requests python-dotenv stripe
2. Set Up Environment Variables:
Create a .env file in the root directory:

ini
Copy
Edit
STRIPE_API_KEY=sk_test_your_stripe_key_here
3. Run the Application:
bash
Copy
Edit
streamlit run app.py
4. Navigate through the App:
Start on the Landing page.

Click Get Started to move to the Login page.

Enter dummy credentials (e.g., user1 / password1).

Upon successful login, you will be redirected to the Map page.

Code Structure Overview:
app.py:

Main application file with page navigation and animation integration.

Uses Streamlit session states for smooth transitions.

06Dashboard.py:

Manages payment processing using Stripe API (key securely stored in .env).

Displays ride fare and redirects to the payment gateway.

assets/

Contains images and other static files for the UI.

Contact
For inquiries or collaboration, feel free to reach out:

Zainab Hassan Chaudhry
Karachi, Pakistan
Email: zainabhchaudhry@gmail.com
LinkedIn: Zainab Hassan Chaudhry

Thank you for considering SHE - a ride-hailing platform designed to empower women, enhance safety, and promote community involvement. Together, let's transform the daily commute for women into a safe and reliable experience.
