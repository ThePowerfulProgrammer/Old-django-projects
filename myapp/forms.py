from django import forms


class NewMovieForm(forms.Form):
    # name for form field
    movie = forms.CharField(max_length=50, label='movie')
    movie.widget.attrs.update({'class': 'form-control'})

    