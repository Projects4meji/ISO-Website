from django.core.management.base import BaseCommand
from certificates.models import Certificate, CertificationStep

class Command(BaseCommand):
    help = 'Populate certificate data with detailed content'

    def handle(self, *args, **options):
        # Certificate data from React component
        certificates_data = {
            'iso-30000': {
                'name': 'ISO 30000:2009',
                'slug': 'iso-30000',
                'description': 'Ship Recycling Management Systems - Comprehensive framework for safe and environmentally sound ship recycling operations',
                'subtitle': 'Ship Recycling Management Systems',
                'icon': 'fas fa-certificate',
                'overview': '''Comprehensive framework for safe and environmentally sound ship recycling operations
Ensures compliance with international regulations and standards
Promotes sustainable practices in the maritime industry
Accredited by International Accreditation Services for Certification Bodies (IASCB)''',
                'benefits': '''Enhanced environmental protection and worker safety
Improved operational efficiency and risk management
Greater competitive advantage in the global market
Access to innovative solutions and advanced analytics''',
                'objectives': '''Understand the principles of ISO 30000:2009 and its application in ship recycling
Learn to implement effective ship recycling management systems
Develop skills in environmental compliance and safety management''',
                'outcomes': '''Ability to design and implement ship recycling management systems
Enhanced understanding of environmental regulations and compliance
Improved skills in risk assessment and documentation''',
                'assessments': '''Multiple-choice quiz on ISO 30000:2009 principles
Case study analysis of ship recycling scenarios
Practical assignment: Draft a ship recycling management plan''',
                'steps': [
                    {'title': 'Document Review', 'description': "Initial assessment of your organization's documentation and processes", 'icon': 'fas fa-file-alt'},
                    {'title': 'Gap Analysis', 'description': 'Identification of areas that need improvement to meet ISO 30000:2009 requirements', 'icon': 'fas fa-clipboard-check'},
                    {'title': 'Implementation', 'description': 'Support in implementing necessary changes and improvements', 'icon': 'fas fa-user-cog'},
                    {'title': 'Certification', 'description': 'Final audit and issuance of certification', 'icon': 'fas fa-award'},
                    {'title': 'Continuous Improvement', 'description': 'Ongoing support and periodic reviews to maintain certification', 'icon': 'fas fa-shield-alt'},
                ]
            },
            'iso-17025': {
                'name': 'ISO/IEC 17025:2005',
                'slug': 'iso-17025',
                'description': 'Testing and Calibration Laboratories - International standard for testing and calibration laboratories',
                'subtitle': 'Testing and Calibration Laboratories',
                'icon': 'fas fa-award',
                'overview': '''International standard for testing and calibration laboratories
Ensures technical competence and reliable results
Globally recognized quality management system
Accredited by International Accreditation Services for Certification Bodies (IASCB)''',
                'benefits': '''International recognition of test results and calibrations
Enhanced customer confidence in laboratory services
Improved operational efficiency and quality control
Access to advanced analytics and risk management tools''',
                'objectives': '''Understand the requirements of ISO/IEC 17025:2005 for testing and calibration laboratories
Learn to implement quality management systems in laboratory settings
Develop skills in technical competence and measurement uncertainty''',
                'outcomes': '''Ability to establish and maintain accredited testing laboratories
Enhanced understanding of quality management principles
Improved skills in technical documentation and calibration procedures''',
                'assessments': '''Written examination on ISO/IEC 17025:2005 requirements
Laboratory audit simulation and case study
Practical assignment: Develop laboratory quality procedures''',
                'steps': [
                    {'title': 'Documentation Review', 'description': 'Assessment of laboratory documentation and quality management system', 'icon': 'fas fa-file-alt'},
                    {'title': 'Technical Assessment', 'description': 'Evaluation of technical competence and testing/calibration procedures', 'icon': 'fas fa-clipboard-check'},
                    {'title': 'Implementation', 'description': 'Support in implementing required changes and improvements', 'icon': 'fas fa-user-cog'},
                    {'title': 'Accreditation', 'description': 'Final assessment and issuance of accreditation', 'icon': 'fas fa-award'},
                    {'title': 'Surveillance', 'description': 'Regular monitoring and periodic reassessment', 'icon': 'fas fa-shield-alt'},
                ]
            },
            'ohsas-8001': {
                'name': 'OHSAS 8001:2007',
                'slug': 'ohsas-8001',
                'description': 'Occupational Health and Safety Management - Comprehensive occupational health and safety management system',
                'subtitle': 'Occupational Health and Safety Management',
                'icon': 'fas fa-medal',
                'overview': '''Comprehensive occupational health and safety management system
Risk assessment and prevention strategies
Employee safety and well-being focus
Designed under Guidelines of OSHA standards''',
                'benefits': '''Reduced workplace incidents and accidents
Enhanced employee morale and productivity
Legal compliance and reduced liability risks
Access to advanced risk management analytics''',
                'objectives': '''Understand OHSAS 8001:2007 requirements for occupational health and safety
Learn to implement effective safety management systems
Develop skills in risk assessment and hazard identification''',
                'outcomes': '''Ability to establish and maintain occupational health and safety systems
Enhanced understanding of workplace safety regulations
Improved skills in risk management and incident prevention''',
                'assessments': '''Safety management system audit and evaluation
Risk assessment case study and practical exercise
Final project: Develop comprehensive safety procedures''',
                'steps': [
                    {'title': 'Initial Review', 'description': 'Assessment of current health and safety management system', 'icon': 'fas fa-file-alt'},
                    {'title': 'Risk Assessment', 'description': 'Comprehensive evaluation of workplace hazards and risks', 'icon': 'fas fa-clipboard-check'},
                    {'title': 'Implementation', 'description': 'Support in implementing required safety measures and procedures', 'icon': 'fas fa-user-cog'},
                    {'title': 'Certification', 'description': 'Final audit and certification issuance', 'icon': 'fas fa-award'},
                    {'title': 'Monitoring', 'description': 'Continuous assessment and improvement of safety measures', 'icon': 'fas fa-shield-alt'},
                ]
            },
            'haccp': {
                'name': 'HACCP',
                'slug': 'haccp',
                'description': 'Hazard Analysis and Critical Control Points - Systematic preventive approach to food safety',
                'subtitle': 'Hazard Analysis and Critical Control Points',
                'icon': 'fas fa-shield-alt',
                'overview': '''Systematic preventive approach to food safety
Identification and control of potential hazards
Internationally recognized food safety standard
Comprehensive food safety management system''',
                'benefits': '''Enhanced food safety and quality control
Reduced risk of foodborne illnesses
Improved customer confidence and market access
Access to innovative food safety solutions''',
                'objectives': '''Understand the principles of HACCP and its application in food safety management
Identify critical control points and implement monitoring procedures
Develop and maintain effective food safety documentation''',
                'outcomes': '''Ability to design and implement a HACCP plan
Improved understanding of food safety hazards and controls
Enhanced skills in risk assessment and documentation''',
                'assessments': '''Multiple-choice quiz on HACCP principles
Case study analysis of a food safety scenario
Practical assignment: Draft a sample HACCP plan''',
                'steps': [
                    {'title': 'Initial Assessment', 'description': 'Review of current food safety practices and documentation', 'icon': 'fas fa-file-alt'},
                    {'title': 'Hazard Analysis', 'description': 'Identification and assessment of potential food safety hazards', 'icon': 'fas fa-clipboard-check'},
                    {'title': 'Implementation', 'description': 'Establishment of critical control points and monitoring procedures', 'icon': 'fas fa-user-cog'},
                    {'title': 'Certification', 'description': 'Final audit and certification issuance', 'icon': 'fas fa-award'},
                    {'title': 'Verification', 'description': 'Ongoing verification and validation of HACCP system', 'icon': 'fas fa-shield-alt'},
                ]
            }
        }

        for slug, data in certificates_data.items():
            cert, created = Certificate.objects.get_or_create(
                slug=slug,
                defaults=data
            )
            
            if created:
                self.stdout.write(f'Created certificate: {cert.name}')
            else:
                # Update existing certificate
                for key, value in data.items():
                    if key != 'steps':
                        setattr(cert, key, value)
                cert.save()
                self.stdout.write(f'Updated certificate: {cert.name}')

            # Create or update steps
            if 'steps' in data:
                # Clear existing steps
                cert.steps.all().delete()
                
                for order, step_data in enumerate(data['steps']):
                    CertificationStep.objects.create(
                        certificate=cert,
                        title=step_data['title'],
                        description=step_data['description'],
                        icon=step_data['icon'],
                        order=order
                    )

        self.stdout.write(self.style.SUCCESS('Successfully populated certificate data!'))
