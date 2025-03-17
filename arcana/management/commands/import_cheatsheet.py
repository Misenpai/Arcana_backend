from django.core.management.base import BaseCommand
from arcana.models import Language, Section, Header, SubHeader

class Command(BaseCommand):
    help = 'Imports cheat sheet data from a text file with sections and links'

    def add_arguments(self, parser):
        parser.add_argument('language', type=str, help='Name of the programming language')
        parser.add_argument('file_path', type=str, help='Path to the text file')

    def handle(self, *args, **options):
        language_name = options['language']
        file_path = options['file_path']

        language, _ = Language.objects.get_or_create(name=language_name)
        current_section = None
        current_header = None

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    line = lines[i].strip()
                    if line.startswith('Link:'):
                        link = line.replace('Link:', '').strip()
                        language.link = link 
                        language.save()
                        self.stdout.write(f'Added link: {link}')
                    elif line.startswith('Section:'):
                        section_title = line.replace('Section:', '').strip()
                        current_section = Section.objects.create(language=language, title=section_title)
                        self.stdout.write(f'Created section: {section_title}')
                        current_header = None 
                    elif line.startswith('Header:'): 
                        if current_section is None:
                            self.stdout.write(self.style.ERROR('Header found before a section'))
                            return
                        header_title = line.replace('Header:', '').strip()
                        current_header = Header.objects.create(section=current_section, title=header_title)
                        self.stdout.write(f'Created header: {header_title}')
                    elif line.startswith('Subheader:'):
                        if current_header is None:
                            self.stdout.write(self.style.ERROR('Subheader found before a header'))
                            return
                        subheader_title = line.replace('Subheader:', '').strip()
                        i += 1
                        description = ''
                        code = ''
                        current_field = None

                        while i < len(lines) and not lines[i].startswith(('Section:', 'Header:', 'Subheader:', 'Link:')):
                            if lines[i].startswith('Description:'):
                                current_field = 'description'
                                description = lines[i].replace('Description:', '').strip() + '\n'
                            elif lines[i].startswith('Code:'):
                                current_field = 'code'
                                code = lines[i].replace('Code:', '').strip() + '\n'
                            elif current_field == 'description':
                                description += lines[i]
                            elif current_field == 'code':
                                code += lines[i]
                            i += 1

                        SubHeader.objects.create(
                            header=current_header,
                            title=subheader_title,
                            content=description.strip(),
                            code=code.strip()
                        )
                        self.stdout.write(f'Created subheader: {subheader_title}')
                        continue
                    i += 1
            self.stdout.write(self.style.SUCCESS(f'Successfully imported cheat sheet for {language_name}'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))