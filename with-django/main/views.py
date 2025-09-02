from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, 'main/home.html')


def home_with_variable(request):
	context = {
		'company_name': 'SpeedPro Performance Services',
		'css_path': 'main/css/home.css',
		'nav_links': [
			{'id': 'services', 'label': 'Services'},
			{'id': 'about', 'label': 'About'},
			{'id': 'contact', 'label': 'Contact'},
			{'id': 'testimonials', 'label': 'Testimonials'},
			{'id': 'case-studies', 'label': 'Case Studies'},
			{'id': 'team', 'label': 'Team'},
			{'id': 'faq', 'label': 'FAQ'},
		],
		'hero_title': 'Accelerate Your Business',
		'hero_description': 'We help companies achieve lightning-fast web performance, robust scalability, and seamless user experiences. Our experts analyze, optimize, and deliver results for your digital platforms.',
		'hero_img': 'main/img/performance.jpg',
		'services': [
			'Web Performance Audits',
			'Load & Stress Testing',
			'Scalability Consulting',
			'CDN & Caching Solutions',
			'Custom Monitoring Dashboards',
		],
		'about_us': "SpeedPro is a team of engineers passionate about speed. With 10+ years of experience, we've helped startups and enterprises unlock their full potential online.",
		'contact_email': 'info@speedpro.com',
		'contact_phone': '+1 555-123-4567',
		'testimonials': [
			{'quote': 'SpeedPro transformed our website’s performance. Our users noticed the difference instantly!', 'author': 'Tech Startup CEO'},
			{'quote': 'Their team is knowledgeable, responsive, and results-driven.', 'author': 'Enterprise CTO'},
		],
		'case_studies': [
			{'title': 'Retail Giant', 'result': 'Improved page load time by 60%, resulting in 30% higher conversion rates.'},
			{'title': 'Fintech Startup', 'result': 'Scaled infrastructure to handle 10x traffic during product launch.'},
		],
		'team': [
			{'name': 'Jane Doe', 'role': 'Lead Performance Engineer'},
			{'name': 'John Smith', 'role': 'Scalability Specialist'},
			{'name': 'Emily Lee', 'role': 'UX Optimization Expert'},
		],
		'faqs': [
			{'q': 'How do I get started?', 'a': 'Contact us for a free initial consultation.'},
			{'q': 'What industries do you serve?', 'a': 'We work with e-commerce, finance, SaaS, and more.'},
			{'q': 'Can you help with legacy systems?', 'a': 'Yes, we specialize in optimizing both modern and legacy platforms.'},
		],
		'year': 2025,
	}
	return render(request, 'main/home_with_variable.html', context)


def ping(request):
	return HttpResponse('pong')
