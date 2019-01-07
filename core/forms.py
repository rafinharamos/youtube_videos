# -*- coding: utf-8 -*-
from datetime import timedelta

from django import forms
from django.utils.translation import ugettext_lazy as _

from core.models import Video, Theme, Thumb, Comment
from django.utils import timezone

ERROR_CSS_CLASS_REFERENCE = 'error_form'
REQUIRED_CSS_CLASS_REFERENCE = 'required_form'


class VideoForm(forms.ModelForm):
    error_css_class = ERROR_CSS_CLASS_REFERENCE
    required_css_class = REQUIRED_CSS_CLASS_REFERENCE
    
    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    def clean_date_uploaded(self):
        date = self.cleaned_data.get('date_uploaded')
        now = timezone.now().date()
        if date:
            if date > now:
                raise forms.ValidationError(_("Please, set a date equal or before today."))
            if date < now - timedelta(days = 365):
                raise forms.ValidationError(_("This video is so old. Please, set a recent video."))
        return date
    
    class Meta:
        model = Video
        fields = '__all__'
    
    
class ThemeForm(forms.ModelForm):
    error_css_class = ERROR_CSS_CLASS_REFERENCE
    required_css_class = REQUIRED_CSS_CLASS_REFERENCE
    
    def __init__(self, *args, **kwargs):
        super(ThemeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Theme
        fields = '__all__'


class ThumbForm(forms.ModelForm):
    error_css_class = ERROR_CSS_CLASS_REFERENCE
    required_css_class = REQUIRED_CSS_CLASS_REFERENCE
    
    def __init__(self, *args, **kwargs):
        super(ThumbForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Thumb
        fields = '__all__'
        
 
class CommentForm(forms.ModelForm):
    error_css_class = ERROR_CSS_CLASS_REFERENCE
    required_css_class = REQUIRED_CSS_CLASS_REFERENCE
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Comment
        fields = '__all__'           
        

