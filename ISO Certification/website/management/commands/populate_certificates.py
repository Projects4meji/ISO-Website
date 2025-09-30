from django.core.management.base import BaseCommand
from website.models import Certificate, CertificationStep


class Command(BaseCommand):
    help = 'Populate certificate data with detailed content'

    def handle(self, *args, **options):
        certificates_data = {
            'iso-30000': {
                'name': 'ISO 30000:2009',
                'slug': 'iso-30000',
                'description': 'Ship Recycling Management Systems - Comprehensive framework for safe and environmentally sound ship recycling operations',
                'subtitle': 'Ship Recycling Management Systems',
                'icon': 'fas fa-certificate',
                'overview': (
                    'Comprehensive framework for safe and environmentally sound ship recycling operations\n'
                    'Ensures compliance with international regulations and standards\n'
                    'Promotes sustainable practices in the maritime industry\n'
                    'Accredited by International Accreditation Services for Certification Bodies (IASCB)'
                ),
                'benefits': (
                    'Enhanced environmental protection and worker safety\n'
                    'Improved operational efficiency and risk management\n'
                    'Greater competitive advantage in the global market\n'
                    'Access to innovative solutions and advanced analytics'
                ),
                'objectives': (
                    'Understand the principles of ISO 30000:2009 and its application in ship recycling\n'
                    'Learn to implement effective ship recycling management systems\n'
                    'Develop skills in environmental compliance and safety management'
                ),
                'outcomes': (
                    'Ability to design and implement ship recycling management systems\n'
                    'Enhanced understanding of environmental regulations and compliance\n'
                    'Improved skills in risk assessment and documentation'
                ),
                'assessments': (
                    'Multiple-choice quiz on ISO 30000:2009 principles\n'
                    'Case study analysis of ship recycling scenarios\n'
                    'Practical assignment: Draft a ship recycling management plan'
                ),
                'steps': [
                    {'title': 'Document Review', 'description': "Initial assessment of your organization's documentation and processes", 'icon': 'fas fa-file-alt'},
                    {'title': 'Gap Analysis', 'description': 'Identification of areas that need improvement to meet ISO 30000:2009 requirements', 'icon': 'fas fa-clipboard-check'},
                    {'title': 'Implementation', 'description': 'Support in implementing necessary changes and improvements', 'icon': 'fas fa-user-cog'},
                    {'title': 'Certification', 'description': 'Final audit and issuance of certification', 'icon': 'fas fa-award'},
                    {'title': 'Continuous Improvement', 'description': 'Ongoing support and periodic reviews to maintain certification', 'icon': 'fas fa-shield-alt'},
                ],
            },
            'iso-17025': {
                'name': 'ISO/IEC 17025:2005',
                'slug': 'iso-17025',
                'description': 'Testing and Calibration Laboratories - International standard for testing and calibration laboratories',
                'subtitle': 'Testing and Calibration Laboratories',
                'icon': 'fas fa-award',
                'overview': (
                    'International standard for testing and calibration laboratories\n'
                    'Ensures technical competence and reliable results\n'
                    'Globally recognized quality management system\n'
                    'Accredited by International Accreditation Services for Certification Bodies (IASCB)'
                ),
                'benefits': (
                    'International recognition of test results and calibrations\n'
                    'Enhanced customer confidence in laboratory services\n'
                    'Improved operational efficiency and quality control\n'
                    'Access to advanced analytics and risk management tools'
                ),
                'objectives': (
                    'Understand the requirements of ISO/IEC 17025:2005 for testing and calibration laboratories\n'
                    'Learn to implement quality management systems in laboratory settings\n'
                    'Develop skills in technical competence and measurement uncertainty'
                ),
                'outcomes': (
                    'Ability to establish and maintain accredited testing laboratories\n'
                    'Enhanced understanding of quality management principles\n'
                    'Improved skills in technical documentation and calibration procedures'
                ),
                'assessments': (
                    'Written examination on ISO/IEC 17025:2005 requirements\n'
                    'Laboratory audit simulation and case study\n'
                    'Practical assignment: Develop laboratory quality procedures'
                ),
                'steps': [
                    {'title': 'Documentation Review', 'description': 'Assessment of laboratory documentation and quality management system', 'icon': 'fas fa-file-alt'},
                    {'title': 'Technical Assessment', 'description': 'Evaluation of technical competence and testing/calibration procedures', 'icon': 'fas fa-clipboard-check'},
                    {'title': 'Implementation', 'description': 'Support in implementing required changes and improvements', 'icon': 'fas fa-user-cog'},
                    {'title': 'Accreditation', 'description': 'Final assessment and issuance of accreditation', 'icon': 'fas fa-award'},
                    {'title': 'Surveillance', 'description': 'Regular monitoring and periodic reassessment', 'icon': 'fas fa-shield-alt'},
                ],
            },
            'ohsas-8001': {
                'name': 'OHSAS 8001:2007',
                'slug': 'ohsas-8001',
                'description': 'Occupational Health and Safety Management - Comprehensive occupational health and safety management system',
                'subtitle': 'Occupational Health and Safety Management',
                'icon': 'fas fa-medal',
                'overview': (
                    'Comprehensive occupational health and safety management system\n'
                    'Risk assessment and prevention strategies\n'
                    'Employee safety and well-being focus\n'
                    'Designed under Guidelines of OSHA standards'
                ),
                'benefits': (
                    'Reduced workplace incidents and accidents\n'
                    'Enhanced employee morale and productivity\n'
                    'Legal compliance and reduced liability risks\n'
                    'Access to advanced risk management analytics'
                ),
                'objectives': (
                    'Understand OHSAS 8001:2007 requirements for occupational health and safety\n'
                    'Learn to implement effective safety management systems\n'
                    'Develop skills in risk assessment and hazard identification'
                ),
                'outcomes': (
                    'Ability to establish and maintain occupational health and safety systems\n'
                    'Enhanced understanding of workplace safety regulations\n'
                    'Improved skills in risk management and incident prevention'
                ),
                'assessments': (
                    'Safety management system audit and evaluation\n'
                    'Risk assessment case study and practical exercise\n'
                    'Final project: Develop comprehensive safety procedures'
                ),
                'steps': [
                    {'title': 'Initial Review', 'description': 'Assessment of current health and safety management system', 'icon': 'fas fa-file-alt'},
                    {'title': 'Risk Assessment', 'description': 'Comprehensive evaluation of workplace hazards and risks', 'icon': 'fas fa-clipboard-check'},
                    {'title': 'Implementation', 'description': 'Support in implementing required safety measures and procedures', 'icon': 'fas fa-user-cog'},
                    {'title': 'Certification', 'description': 'Final audit and certification issuance', 'icon': 'fas fa-award'},
                    {'title': 'Monitoring', 'description': 'Continuous assessment and improvement of safety measures', 'icon': 'fas fa-shield-alt'},
                ],
            },
            'haccp': {
                'name': 'HACCP',
                'slug': 'haccp',
                'description': 'Hazard Analysis and Critical Control Points - Systematic preventive approach to food safety',
                'subtitle': 'Hazard Analysis and Critical Control Points',
                'icon': 'fas fa-shield-alt',
                'overview': (
                    'Systematic preventive approach to food safety\n'
                    'Identification and control of potential hazards\n'
                    'Internationally recognized food safety standard\n'
                    'Comprehensive food safety management system'
                ),
                'benefits': (
                    'Enhanced food safety and quality control\n'
                    'Reduced risk of foodborne illnesses\n'
                    'Improved customer confidence and market access\n'
                    'Access to innovative food safety solutions'
                ),
                'objectives': (
                    'Understand the principles of HACCP and its application in food safety management\n'
                    'Identify critical control points and implement monitoring procedures\n'
                    'Develop and maintain effective food safety documentation'
                ),
                'outcomes': (
                    'Ability to design and implement a HACCP plan\n'
                    'Improved understanding of food safety hazards and controls\n'
                    'Enhanced skills in risk assessment and documentation'
                ),
                'assessments': (
                    'Multiple-choice quiz on HACCP principles\n'
                    'Case study analysis of a food safety scenario\n'
                    'Practical assignment: Draft a sample HACCP plan'
                ),
                'steps': [
                    {'title': 'Initial Assessment', 'description': 'Review of current food safety practices and documentation', 'icon': 'fas fa-file-alt'},
                    {'title': 'Hazard Analysis', 'description': 'Identification and assessment of potential food safety hazards', 'icon': 'fas fa-clipboard-check'},
                    {'title': 'Implementation', 'description': 'Establishment of critical control points and monitoring procedures', 'icon': 'fas fa-user-cog'},
                    {'title': 'Certification', 'description': 'Final audit and certification issuance', 'icon': 'fas fa-award'},
                    {'title': 'Verification', 'description': 'Ongoing verification and validation of HACCP system', 'icon': 'fas fa-shield-alt'},
                ],
            },
        }

        for slug, data in certificates_data.items():
            cert, created = Certificate.objects.get_or_create(
                slug=slug,
                defaults={k: v for k, v in data.items() if k != 'steps'},
            )

            if not created:
                for key, value in data.items():
                    if key != 'steps':
                        setattr(cert, key, value)
                cert.save()

            cert.steps.all().delete()
            for order, step in enumerate(data.get('steps', [])):
                CertificationStep.objects.create(
                    certificate=cert,
                    title=step['title'],
                    description=step['description'],
                    icon=step['icon'],
                    order=order,
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated certificate data!'))
