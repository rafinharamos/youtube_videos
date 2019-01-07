# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Video(models.Model):

    title = models.CharField(_("Title"), max_length = 50, 
                             help_text = _("Title of video."))
    date_uploaded = models.DateField(_("Date"), 
    help_text = _("The date it was uploaded. (Make sure that videos that are more "
                  "than 1 year old should not be added, as they are less relevant)."))
    views = models.FloatField(_("Views"), 
                              help_text = _("The amount of views the video received."))
    themes = models.ManyToManyField("core.Theme", verbose_name = _("Themes."))
    
    class Meta:
        app_label = 'core'
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        
    def __str__(self):
        return self.title

    def score(self):
        return self.views * self.time_factor() * self.positivity_factor()
    
    def positivity_factor(self):
        return 0.7 * self.good_comments() + 0.3 * self.thumbs_up()
    
    def days_since_upload(self):
        return (timezone.now().date() - self.date_uploaded).days
    
    def time_factor(self):
        return max(0, 1 - (self.days_since_upload()/365))
    
    def good_comments(self):
        positive_comments = self.get_positive_comments()
        negative_comments = self.get_negative_comments()
        if positive_comments:
            return positive_comments/(positive_comments+negative_comments)
        else:
            return 0
        
    def thumbs_up(self):
        thumbs_up = self.get_thumbs_up()
        thumbs_down = self.get_thumbs_down()
        if thumbs_up:
            return thumbs_up/(thumbs_up+thumbs_down)
        return 0
    
    def get_positive_comments(self):
        """
            Get positives comments about the video.
        """
        return self.comment_set.filter(is_positive = True).count()
                
    def get_negative_comments(self):
        """
            Get negatives comments about the video.
        """
        return self.comment_set.filter(is_positive = False).count()
    
    def get_thumbs_up(self):
        """
            Get thumbs up about the video.
        """
        return self.thumb_set.filter(is_positive = True).count()
    
    def get_thumbs_down(self):
        """
            Get thumbs down about the video.
        """
        return self.thumb_set.filter(is_positive = False).count()
    
    
class Theme(models.Model):

    title = models.CharField(_("Title"), max_length = 50, help_text = _("Title of theme."))
    
    class Meta:
        app_label = 'core'
        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'
        
    def __str__(self):
        return self.title
    
    def score(self):
        score = 0
        videos = self.video_set.all()
        for video in videos:
            score += video.score()
        return score

class Thumb(models.Model):

    is_positive = models.BooleanField(_("Is positive?"), 
        help_text = _("Whether or not this is a positive thumb."))
    time = models.TimeField(auto_now_add = True, 
                            help_text = _("The time when the thumbs up or down was given."))
    video = models.ForeignKey("core.Video", verbose_name = _("The video referenced by this thumb."))
    
    class Meta:
        app_label = 'core'
        verbose_name = 'Thumb'
        verbose_name_plural = 'Thumbs'
        
    def __str__(self):
        return "{} - Positive: {}".format(self.video.title, self.is_positive)
    
    
class Comment(models.Model):

    is_positive = models.BooleanField(_("Is positive?"), 
                            help_text = _("Whether or not this is a positive comment."))
    time = models.TimeField(auto_now_add = True, 
                            help_text = _("The time when the comment was written."))
    video = models.ForeignKey("core.Video", 
                              verbose_name = _("The video referenced by this comment."))
    
    class Meta:
        app_label = 'core'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        
    def __str__(self):
        return "{} - Positive: {}".format(self.video.title, self.is_positive)
    
    
    