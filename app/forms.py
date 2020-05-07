from django import forms
from django.core.files.storage import default_storage

class SingleUploadForm(forms.Form):
    file = forms.ImageField(label='image file')

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name)

class BaseUploadFormSet(forms.BaseFormSet):

    def save(self):
        # a list will be generated like ['/media/1.png', '/media/2.png']
        url_list = []

        # In models.py, file = forms.ImageField(label='image file')
        # you can access forms
        # call each form.saves() in SingleUploadForm to collect file URLs
        # # form.save() gives file's URL path, ant put it into context
        for form in self.forms:
            try:
                url = form.save()
            except KeyError:
                # If no files is uploaded, form has KeyError, so ignore it
                pass
            else:
                url_list.append(url)
        return url_list


UploadFormSet = forms.formset_factory(SingleUploadForm, formset=BaseUploadFormSet, extra=5)