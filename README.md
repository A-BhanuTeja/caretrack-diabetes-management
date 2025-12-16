# 🏥 CareTrack - Diabetes Management System

A comprehensive full-stack web application for diabetes management with personalized diet plans and interactive data visualization.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

### Core Functionality
- ✅ **Patient Management** - Register and manage patient profiles with automatic BMI calculation
- ✅ **Blood Sugar Tracking** - Record fasting and post-meal glucose levels with date tracking
- ✅ **Interactive Dashboards** - Visualize sugar trends with beautiful Plotly graphs
- ✅ **Personalized Diet Plans** - Get customized meal recommendations based on your readings
- ✅ **Health Metrics** - Track cholesterol and thyroid levels
- ✅ **Historical Records** - View complete reading history with color-coded status indicators
- ✅ **Admin Panel** - Comprehensive data management interface

### Advanced Features
- 📊 Real-time data visualization with interactive line charts
- 🍽️ Time-specific meal plans (breakfast, mid-morning, lunch, evening, dinner, bedtime)
- 💡 Smart recommendations based on age, BMI, and current sugar levels
- 📈 Statistical analysis showing averages, min/max values, and trends
- 🎨 Responsive design works on desktop, tablet, and mobile
- 🔐 Secure admin authentication
- 📱 Mobile-friendly Bootstrap 5 interface

## 🛠️ Technologies Used

### Backend
- **Python 3.8+**
- **Django 4.2** - Full-stack web framework
- **SQLite** - Lightweight database

### Frontend
- **HTML5, CSS3, JavaScript**
- **Bootstrap 5** - Modern responsive UI
- **Font Awesome** - Beautiful icons

### Libraries
- **Plotly** - Interactive data visualization and charts
- **django-crispy-forms** - Beautiful form rendering
- **crispy-bootstrap4** - Bootstrap styling for forms

## 📦 Installation & Setup

### Prerequisites
```bash
Python 3.8 or higher
pip (Python package manager)
Git
```

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/A-BhanuTeja/caretrack-diabetes-management.git
cd caretrack-diabetes-management
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser (admin account)**
```bash
python manage.py createsuperuser
# Follow the prompts to set username and password
```

6. **Run the development server**
```bash
python manage.py runserver
```

7. **Access the application**
- **Main Application:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## 🚀 Usage

### For Patients
1. Register a new patient with name, age, weight, and height
2. Add daily blood sugar readings (fasting and post-meal)
3. View personalized diet plans based on your readings
4. Track your progress with interactive graphs
5. Monitor trends over time

### For Healthcare Providers
1. Manage multiple patients from the admin panel
2. Review patient history and statistics
3. Export data for analysis
4. Track compliance and health improvements

## 📊 Project Structure
```
caretrack-diabetes-management/
├── CareTrack/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app/                    # Main application
│   ├── models.py          # Database models
│   ├── views.py           # Business logic
│   ├── forms.py           # Form definitions
│   ├── diet_plans.py      # Diet recommendation engine
│   ├── admin.py           # Admin configuration
│   ├── templates/         # HTML templates
│   └── migrations/        # Database migrations
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── LICENSE               # MIT License
└── README.md            # This file
```

## 💡 Key Features Explained

### Smart Diet Plans
The system analyzes three key factors:
- **Blood Sugar Levels** (High/Normal/Low)
- **Patient Age** (Different recommendations for seniors vs. young adults)
- **BMI** (Body Mass Index for weight management)

Based on these, it generates:
- 6 meal plans per day (breakfast through bedtime snack)
- Multiple options for each meal
- Calorie information
- Foods to eat and avoid
- Hydration guidelines
- Exercise recommendations

### Data Visualization
- Interactive Plotly charts showing 30-day trends
- Color-coded status indicators
- Statistical summaries (averages, min/max)
- Historical data tables

## 🎯 Use Cases

- **Individual Diabetes Patients** - Track daily sugar levels and get meal guidance
- **Family Members** - Help elderly relatives manage their diabetes
- **Healthcare Clinics** - Monitor multiple patients efficiently
- **Dietitians** - Provide data-driven meal recommendations
- **Researchers** - Analyze diabetes management patterns

## 🔐 Security Features

- CSRF protection (built into Django)
- SQL injection prevention (Django ORM)
- XSS (Cross-Site Scripting) protection
- Secure password hashing with PBKDF2
- Admin-only access to sensitive data

## 📈 Database Schema

### Models
1. **Patient**
   - Personal info (name, age, weight, height)
   - Auto-calculated BMI
   - Timestamps

2. **SugarReading**
   - Fasting sugar level
   - Post-meal sugar level
   - Date and notes
   - Foreign key to Patient

3. **HealthData**
   - Cholesterol levels (total, LDL, HDL)
   - Thyroid (TSH) level
   - Foreign key to Patient

## 🚀 Future Enhancements

Planned features for future versions:

- [ ] User authentication system for multiple families
- [ ] Email/SMS alerts for abnormal readings
- [ ] PDF export for medical reports
- [ ] Medicine reminder system
- [ ] Doctor appointment scheduling
- [ ] Integration with glucose meter APIs
- [ ] Mobile app (React Native)
- [ ] Multi-language support (Hindi, Telugu, Tamil)
- [ ] AI-powered predictions and insights
- [ ] Cloud deployment (AWS/Heroku)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This means you can freely use, modify, and distribute this software.

## 👨‍💻 Developer

**Bhanu Teja Amudala**
- GitHub: [@A-BhanuTeja](https://github.com/A-BhanuTeja)
- LinkedIn: [Connect with me](https://linkedin.com/in/your-profile) <!-- Add your LinkedIn -->
- Email: your.email@example.com <!-- Add your email -->

*2024 Computer Science Graduate | Python Full-Stack Developer*

## 🙏 Acknowledgments

- Inspired by the need for accessible diabetes management tools
- Built with Django framework and its amazing community
- Bootstrap for beautiful, responsive UI components
- Plotly for powerful data visualization
- All open-source contributors

## 📞 Support & Contact

- **Issues:** Open an issue on GitHub
- **Email:** your.email@example.com
- **Documentation:** See the code comments for detailed explanations

## ⭐ Show Your Support

If you found this project helpful or interesting, please give it a star! ⭐

It helps others discover the project and motivates further development.

---

**Built with ❤️ for better diabetes management**
