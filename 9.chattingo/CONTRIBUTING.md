# 🤝 Contributing to Chattingo Hackathon

## 📋 Table of Contents

- [Development Setup](#-development-setup)
- [Environment Configuration](#-environment-configuration)
- [Production Deployment](#-production-deployment)
- [Task Checklist](#-task-checklist)
- [Submission Guide](#-submission-guide)

---

## 🚀 Development Setup

### Prerequisites
- **Java 17+** (OpenJDK recommended)
- **Node.js 18+** 
- **MySQL 8.0+**
- **Git** (for version control)

### Quick Start for Hackathon Participants

#### **Step 1: Fork & Clone the Repository**
```bash
# 1. Fork this repository on GitHub: https://github.com/iemafzalhassan/chattingo
# 2. Clone your fork locally
git clone https://github.com/YOUR_USERNAME/chattingo.git
cd chattingo
```

#### **Step 2: Install Dependencies**

**On macOS:**
```bash
# Install Java 17
brew install openjdk@17
echo 'export PATH="/opt/homebrew/opt/openjdk@17/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Install MySQL
brew install mysql
brew services start mysql

# Verify installations
java -version
node -v
mysql --version
```

**On Ubuntu/Debian:**
```bash
# Install Java 17
sudo apt update
sudo apt install openjdk-17-jdk

# Install Node.js 18
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install MySQL
sudo apt install mysql-server
sudo systemctl start mysql
```

**On Windows:**
```bash
# Download and install from official websites:
# - Java 17: https://adoptium.net/
# - Node.js 18: https://nodejs.org/
# - MySQL: https://dev.mysql.com/downloads/mysql/
```

#### **Step 3: Setup Database**
```bash
# Connect to MySQL (no password for fresh install)
mysql -u root

# Create database
CREATE DATABASE chattingo_db;
exit
```

#### **Step 4: Configure Backend**
```bash
cd backend

# Copy environment template
cp .env.example .env

# Generate secure JWT secret
openssl rand -base64 64

# Edit .env file with your values:
# JWT_SECRET=<your-generated-secret>
# SPRING_DATASOURCE_PASSWORD= (leave empty for local MySQL)
```

#### **Step 5: Start Backend**
```bash
# From backend directory
./mvnw spring-boot:run
```

#### **Step 6: Start Frontend**
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

#### **Step 7: Verify Setup**
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8080
- **Test signup**: Create a new user account

### Development Workflow

#### **Making Changes**
1. **Backend changes**: Restart with `./mvnw spring-boot:run`
2. **Frontend changes**: Hot reload automatically updates
3. **Database changes**: Hibernate auto-updates schema

#### **Testing API Endpoints**
```bash
# Test signup
curl -X POST http://localhost:8080/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"fullName":"Test User","email":"test@example.com","password":"password123"}'

# Test login
curl -X POST http://localhost:8080/auth/signin \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'
```

### Common Issues & Solutions

#### **"Java not found"**
```bash
# macOS
brew install openjdk@17
export PATH="/opt/homebrew/opt/openjdk@17/bin:$PATH"

# Ubuntu
sudo apt install openjdk-17-jdk

# Windows
# Download from https://adoptium.net/
```

#### **"MySQL connection refused"**
```bash
# Start MySQL service
# macOS: brew services start mysql
# Ubuntu: sudo systemctl start mysql
# Windows: Start MySQL service from Services

# Create database
mysql -u root -e "CREATE DATABASE chattingo_db;"
```

#### **"JWT secret too short"**
```bash
# Generate proper secret
openssl rand -base64 64
# Copy output to JWT_SECRET in .env
```

#### **"CORS errors in browser"**
- Verify `CORS_ALLOWED_ORIGINS` includes your frontend URL
- Restart backend after changing CORS settings

#### **"Port already in use"**
```bash
# Find and kill process using port
lsof -ti:8080 | xargs kill -9  # Backend
lsof -ti:3000 | xargs kill -9  # Frontend
```

#### **"npm install fails"**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

---

## ⚙️ Environment Configuration

### Required Configuration Files

You need to configure these essential files before running the application:

- **Backend Environment**: `backend/.env`
- **Frontend Environment**: `frontend/.env`

### Backend Configuration (`backend/.env`)

Create a `.env` file in the `backend/` directory with these required variables:

**Security Settings (Required)**
- `JWT_SECRET`: A 64-character secret key for JWT token generation
- `MYSQL_ROOT_PASSWORD`: A secure password for your MySQL database

**Domain Settings (Required)**
- `CORS_ALLOWED_ORIGINS`: Your frontend domain(s) for CORS policy
- `SPRING_DATASOURCE_URL`: Database connection URL

**Database Settings (Default)**
- `SPRING_DATASOURCE_USERNAME`: Database username (default: root)
- `MYSQL_DATABASE`: Database name (default: chattingo_db)

### Frontend Configuration (`frontend/.env`)

Create a `.env` file in the `frontend/` directory:

**API Configuration (Required)**
- `REACT_APP_API_URL`: Your backend API URL

### Generating Secure Secrets

**JWT Secret**: Generate a 64-character random string for JWT token signing
**Database Password**: Create a strong password for your MySQL root user

### CORS Configuration

Configure Cross-Origin Resource Sharing (CORS) to allow your frontend to communicate with the backend:

**Single Domain**: Use your main domain
**Multiple Domains**: Separate multiple domains with commas
**Development**: Include localhost URLs for local development

### Environment Variables Reference

#### Required Variables

| Variable | Description | Purpose |
|----------|-------------|---------|
| `JWT_SECRET` | 64-character secret for JWT tokens | Secure token generation |
| `MYSQL_ROOT_PASSWORD` | Database root password | Database security |
| `CORS_ALLOWED_ORIGINS` | Allowed frontend domains | Cross-origin security |
| `REACT_APP_API_URL` | Backend API URL | Frontend-backend communication |

#### Optional Variables

| Variable | Description | Default Value |
|----------|-------------|---------------|
| `SERVER_PORT` | Backend server port | `8080` |
| `MYSQL_DATABASE` | Database name | `chattingo_db` |
| `SPRING_PROFILES_ACTIVE` | Spring application profile | `production` |

---

## 🌐 Production Deployment

### Quick Deployment Checklist (Sept 7-10)

**Prerequisites**: Complete local development setup from above

#### Task 1: Configure Domain 
1. **Copy environment template:**
```bash
cp .env.example .env
```

2. **Edit .env file with your domain:**
```bash
# Replace with your actual domain
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
REACT_APP_API_URL=https://yourdomain.com
```

#### Task 2: Generate Secrets 
```bash
# Generate JWT secret (copy the output)
openssl rand -base64 64

# Generate database password (copy the output)
openssl rand -base64 32

# Update .env file with generated values
JWT_SECRET=your-generated-jwt-secret-here
MYSQL_ROOT_PASSWORD=your-generated-db-password-here
```

#### Task 3: Create Docker Configuration (Your Task)
You need to create these files:

1. **Frontend Dockerfile** (3-stage build with Nginx)
2. **Backend Dockerfile** (3-stage build with Maven)
3. **docker-compose.yml** (Root level orchestration)
4. **nginx.conf** (Frontend configuration)

#### Task 4: Deploy Application
```bash
# Deploy with production configuration
docker-compose -f docker-compose.prod.yml up -d

# Check if all services are running
docker-compose -f docker-compose.prod.yml ps

# Test backend API
curl http://localhost:8080/actuator/health

# Test frontend
curl http://localhost:80
```

#### Task 5: Setup SSL
```bash
# Install certbot
sudo apt install certbot python3-certbot-nginx -y

# Get SSL certificate (replace with your domain)
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Test HTTPS
curl -I https://yourdomain.com
```

#### Task 6: Final Testing
```bash
# Test user registration
curl -X POST https://yourdomain.com/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"fullName":"Test User","email":"test@example.com","password":"password123"}'

# Open in browser and test chat functionality
# https://yourdomain.com
```

### VPS Setup Requirements

#### Hostinger VPS Setup
- **Server Requirements**: Ubuntu 22.04 LTS, ports 22/80/443/8080
- **Install Docker and Docker Compose**
- **Install Jenkins**
- **Configure firewall**

#### Domain Configuration
- Purchase/configure domain
- Set up DNS records (A records)
- Point domain to VPS IP
- Configure www subdomain

#### SSL Certificate
- Install Certbot
- Generate SSL certificates
- Configure Nginx for HTTPS
- Test SSL configuration

### Troubleshooting

#### Problem: "Docker not found"
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
# Logout and login again
```

#### Problem: "CORS Error in browser"
```bash
# Check your .env file
cat .env | grep CORS_ALLOWED_ORIGINS
# Make sure it matches your exact domain
# Restart backend
docker-compose -f docker-compose.prod.yml restart appservice
```

#### Problem: "SSL certificate failed"
```bash
# Check DNS propagation
dig yourdomain.com
# Make sure it points to your server IP
# Wait up to 2 hours for DNS propagation
```

#### Problem: "Backend not responding"
```bash
# Check backend logs
docker-compose -f docker-compose.prod.yml logs appservice

# Check if database is running
docker-compose -f docker-compose.prod.yml logs dbservice

# Restart all services
docker-compose -f docker-compose.prod.yml restart
```

---

## ✅ Task Checklist

### **Task 1: Docker Implementation (5 Marks)**

#### **Frontend Dockerfile** (3-stage build)
- [ ] Stage 1: Node.js build environment
- [ ] Stage 2: Build React application
- [ ] Stage 3: Nginx runtime server
- [ ] Copy built files to Nginx
- [ ] Configure Nginx for React routing
- [ ] Expose port 80

#### **Backend Dockerfile** (3-stage build)
- [ ] Stage 1: Maven build environment
- [ ] Stage 2: Build Spring Boot application
- [ ] Stage 3: JRE runtime
- [ ] Copy JAR file to runtime
- [ ] Expose port 8080
- [ ] Configure startup command

#### **Docker Compose** (Root level)
- [ ] Define frontend service
- [ ] Define backend service
- [ ] Define database service
- [ ] Configure networking
- [ ] Add health checks
- [ ] Set environment variables

#### **Nginx Configuration**
- [ ] Create nginx.conf file
- [ ] Configure React routing
- [ ] Set up reverse proxy for API
- [ ] Configure static file serving

**Scoring**: Single Stage (2), Two Stage (4), Multi Stage (5)

### **Task 2: Jenkins CI/CD Pipeline (17 Marks)**

#### **Pipeline Stages**
- [ ] **Git Clone** (2 Marks) - Clone repository from GitHub
- [ ] **Image Build** (2 Marks) - Build Docker images
- [ ] **Filesystem Scan** (2 Marks) - Security scan of source code
- [ ] **Image Scan** (2 Marks) - Vulnerability scan of Docker images
- [ ] **Push to Registry** (2 Marks) - Push to Docker Hub/Registry
- [ ] **Update Compose** (2 Marks) - Update docker-compose with new tags
- [ ] **Deploy** (5 Marks) - Deploy to Hostinger VPS

#### **Additional Requirements**
- [ ] **Jenkins Shared Library** (3 Marks) - Reusable components
- [ ] **GitHub Webhook** - Trigger pipeline on code push
- [ ] **Automated Testing** - Run tests before deployment
- [ ] **Rollback Capability** - Ability to rollback deployments

### **Task 3: Documentation (10 Marks)**

#### **README.md** (3 Marks - Compulsory)
- [ ] Project overview
- [ ] Technology stack
- [ ] Installation instructions
- [ ] Deployment guide
- [ ] API documentation
- [ ] Troubleshooting section

#### **Blog Post** (2 Marks - Optional)
- [ ] Technical implementation details
- [ ] Challenges faced and solutions
- [ ] Learning outcomes
- [ ] Code snippets and explanations
- [ ] Deployment process walkthrough

#### **Video Demo** (5 Marks - Compulsory)
- [ ] Local Docker setup demonstration
- [ ] Jenkins pipeline execution
- [ ] Live application walkthrough
- [ ] Key features demonstration
- [ ] Production deployment showcase

### **Task 4: Testing & Validation**

#### **Local Testing**
- [ ] Docker containers build successfully
- [ ] Application runs locally
- [ ] All features work (auth, chat, etc.)
- [ ] Database connectivity
- [ ] API endpoints functional

#### **Production Testing**
- [ ] HTTPS working correctly
- [ ] Domain accessible
- [ ] User registration works
- [ ] User login works
- [ ] Real-time chat functional
- [ ] Group chat creation works
- [ ] Profile management works

#### **Performance Testing**
- [ ] Application loads quickly
- [ ] Real-time updates work
- [ ] Multiple users can chat
- [ ] Database performance
- [ ] Memory usage acceptable

---

## 📤 Submission Guide

### **Submission Requirements**

#### **Required Submission Fields**
1. **Name** - Your full name
2. **Email ID** - Contact email
3. **GitHub Repository URL** - Your forked and implemented project
4. **Video Demo URL** - 3-minute demo video (YouTube/Drive link)
5. **Live Application URL** - Your deployed application on VPS
6. **Blog URL** - Technical writeup (Optional but recommended)
7. **README URL** - Link to your updated README file

#### **Required Deliverables**
1. **GitHub Repository** with your implementation
   - ✅ Dockerfiles (Backend & Frontend - 3-stage builds)
   - ✅ docker-compose.yml (Root level orchestration)
   - ✅ Jenkinsfile (Complete CI/CD pipeline)
   - ✅ nginx.conf (Frontend configuration)
   - ✅ Environment configurations
   - ✅ Updated README with deployment instructions

2. **Live Application** deployed on Hostinger VPS
   - ✅ Working chat application with HTTPS
   - ✅ SSL certificate configured
   - ✅ Domain properly configured
   - ✅ All features functional (registration, login, messaging)

3. **Video Demo** (3 minutes max) showing:
   - ✅ Local Docker setup demonstration
   - ✅ Jenkins pipeline execution
   - ✅ Live application walkthrough on VPS
   - ✅ Key features demonstration

### **Final Checklist**

#### **Before Sept 10, 11:59 PM**
- [ ] All tasks completed
- [ ] Application deployed and working
- [ ] Video demo recorded and uploaded
- [ ] Documentation complete
- [ ] Submission form filled
- [ ] GitHub repository public and accessible

#### **Quality Assurance**
- [ ] Code follows best practices
- [ ] Security measures implemented
- [ ] Error handling in place
- [ ] Logging configured
- [ ] Monitoring setup (optional)

### **Submission Form**
📤 **[Submit Here](https://forms.gle/ww3vPN29JTNRqzM27)** before Sept 10, 11:59 PM

**Total Possible Marks: 39**
- Docker Implementation: 5 marks
- Jenkins Pipeline: 17 marks
- Jenkins Shared Library: 3 marks
- Active Engagement: 2 marks
- Creativity: 2 marks
- Documentation: 10 marks

---

## 💡 Tips for Beginners

### **Git Workflow**
```bash
# Create a new branch for your work
git checkout -b feature/docker-implementation

# Make your changes
# ... edit files ...

# Commit your changes
git add .
git commit -m "Add Docker implementation"

# Push to your fork
git push origin feature/docker-implementation

# Create Pull Request on GitHub
```

### **Testing Your Changes**
- Always test locally before committing
- Use the provided API endpoints for testing
- Check browser console for frontend errors
- Monitor backend logs for issues

### **Getting Help**
- Join Discord channels for support
- Check existing issues on GitHub
- Review the documentation thoroughly
- Test with simple examples first

---

**Good luck with your hackathon project! 🚀**
