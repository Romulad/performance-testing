from django.core.management.base import BaseCommand
from django.utils import timezone
from blog.models import Article
import random
from datetime import timedelta


class Command(BaseCommand):
    help = 'Populate the database with 100 sample articles'

    def handle(self, *args, **options):
        # Clear existing articles
        Article.objects.all().delete()
        
        # Sample data
        tags = [
            'Technology', 'Programming', 'Web Development', 'Django', 'Python',
            'JavaScript', 'React', 'Database', 'Performance', 'Security',
            'DevOps', 'Cloud', 'AI', 'Machine Learning', 'Data Science'
        ]
        
        titles = [
            'Getting Started with Django Performance Optimization',
            'Advanced Python Techniques for Web Development',
            'Building Scalable Web Applications',
            'Database Query Optimization Strategies',
            'Modern JavaScript Frameworks Comparison',
            'Implementing Caching in Django Applications',
            'Security Best Practices for Web Apps',
            'Docker and Containerization Guide',
            'Cloud Deployment Strategies',
            'API Design and Development',
            'Testing Strategies for Django Projects',
            'Frontend Performance Optimization',
            'Machine Learning Integration in Web Apps',
            'Real-time Applications with WebSockets',
            'Microservices Architecture Patterns',
            'Database Design Fundamentals',
            'Authentication and Authorization',
            'Monitoring and Logging Best Practices',
            'CI/CD Pipeline Implementation',
            'Progressive Web Applications',
            'GraphQL vs REST APIs',
            'Serverless Computing Introduction',
            'Data Visualization Techniques',
            'Mobile-First Design Principles',
            'SEO Optimization for Web Apps',
            'Cross-Platform Development',
            'Version Control Best Practices',
            'Code Review Guidelines',
            'Performance Testing Methodologies',
            'Accessibility in Web Development',
            'Responsive Design Techniques',
            'State Management in React',
            'Django ORM Advanced Features',
            'Async Programming in Python',
            'Web Security Vulnerabilities',
            'Load Balancing Strategies',
            'Content Delivery Networks',
            'Database Indexing Strategies',
            'Error Handling Best Practices',
            'Code Documentation Standards',
            'Agile Development Methodologies',
            'User Experience Design',
            'A/B Testing Implementation',
            'Analytics and Metrics',
            'Backup and Recovery Strategies',
            'Scaling Database Systems',
            'Memory Management Optimization',
            'Network Security Fundamentals',
            'Open Source Contribution Guide',
            'Career Development in Tech'
        ]
        
        descriptions = [
            'Learn essential techniques to boost your application performance',
            'Discover advanced patterns and practices for professional development',
            'Build applications that can handle millions of users',
            'Optimize your database queries for maximum efficiency',
            'Compare popular frameworks and choose the right one',
            'Implement effective caching strategies for better performance',
            'Protect your applications from common security threats',
            'Master containerization for consistent deployments',
            'Deploy your applications to the cloud effectively',
            'Design robust and scalable APIs for your applications',
            'Implement comprehensive testing strategies',
            'Optimize frontend performance for better user experience',
            'Integrate AI and ML capabilities into your web apps',
            'Build real-time features with modern technologies',
            'Design scalable microservices architectures',
            'Learn database design principles and best practices',
            'Implement secure authentication and authorization',
            'Monitor and debug your applications effectively',
            'Automate your deployment pipeline for efficiency',
            'Build fast, reliable web applications',
            'Choose the right API architecture for your needs',
            'Explore serverless computing benefits and challenges',
            'Create compelling data visualizations',
            'Design applications that work great on mobile devices',
            'Improve your search engine rankings',
            'Build applications for multiple platforms',
            'Master Git and collaboration workflows',
            'Conduct effective code reviews',
            'Test your application performance under load',
            'Make your applications accessible to everyone',
            'Create responsive designs that work everywhere',
            'Manage application state effectively',
            'Master Django ORM for complex queries',
            'Write efficient asynchronous Python code',
            'Identify and fix security vulnerabilities',
            'Distribute load across multiple servers',
            'Speed up content delivery worldwide',
            'Optimize database performance with proper indexing',
            'Handle errors gracefully in your applications',
            'Write clear and maintainable documentation',
            'Implement agile practices in your team',
            'Design intuitive user interfaces',
            'Test different versions of your application',
            'Track and analyze user behavior',
            'Protect your data with proper backup strategies',
            'Scale your database to handle growth',
            'Optimize memory usage in your applications',
            'Secure your network infrastructure',
            'Contribute to open source projects effectively',
            'Advance your career in the technology industry'
        ]
        
        content_templates = [
            "This comprehensive guide covers everything you need to know about {}. We'll explore the fundamentals, best practices, and advanced techniques that will help you master this important topic.\n\nKey concepts include:\n- Understanding the basics\n- Implementation strategies\n- Common pitfalls to avoid\n- Performance considerations\n- Real-world examples\n\nBy the end of this article, you'll have a solid understanding of how to apply these concepts in your own projects.",
            
            "In today's fast-paced development environment, {} has become increasingly important. This article provides practical insights and actionable advice for developers at all levels.\n\nWe'll cover:\n- Current industry trends\n- Tools and technologies\n- Step-by-step implementation\n- Testing and validation\n- Maintenance and updates\n\nWhether you're a beginner or an experienced developer, you'll find valuable information to improve your skills.",
            
            "Mastering {} is essential for modern web development. This detailed tutorial walks you through the process from start to finish, with practical examples and expert tips.\n\nTopics covered:\n- Planning and preparation\n- Implementation details\n- Optimization techniques\n- Troubleshooting common issues\n- Future considerations\n\nFollow along with our examples and you'll be implementing these techniques in your own projects in no time."
        ]
        
        # Create 100 articles
        for i in range(100):
            # Select random data
            title = titles[i] if i < len(titles) else f"Advanced Topic {i+1}: Technical Deep Dive"
            tag = random.choice(tags)
            description = descriptions[i] if i < len(descriptions) else f"Explore advanced concepts and techniques in {tag.lower()}"
            content = random.choice(content_templates).format(tag.lower())
            
            # Create random date within the last 365 days
            days_ago = random.randint(0, 365)
            article_date = timezone.now() - timedelta(days=days_ago)
            
            # Create the article
            Article.objects.create(
                title=title,
                description=description,
                content=content,
                date=article_date,
                tag=tag
            )
            
            self.stdout.write(f'Created article: {title}')
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created 100 articles!')
        )
