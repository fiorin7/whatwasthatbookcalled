# Generated by Django 3.2.5 on 2021-07-27 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20210724_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, choices=[('Other', 'Other'), ('Acehnese', 'Acehnese'), ('Afrikaans', 'Afrikaans'), ('Albanian', 'Albanian'), ('Alemannic', 'Alemannic'), ('Amharic', 'Amharic'), ('Arabic', 'Arabic'), ('Aragonese', 'Aragonese'), ('Armenian', 'Armenian'), ('Asturian', 'Asturian'), ('Azerbaijani', 'Azerbaijani'), ('Banyumasan', 'Banyumasan'), ('Bashkir', 'Bashkir'), ('Basque', 'Basque'), ('Bavarian', 'Bavarian'), ('Belarusian', 'Belarusian'), ('Bengali', 'Bengali'), ('Bishnupriya Manipuri', 'Bishnupriya Manipuri'), ('Bosnian', 'Bosnian'), ('Breton', 'Breton'), ('Buginese', 'Buginese'), ('Bulgarian', 'Bulgarian'), ('Burmese', 'Burmese'), ('Cantonese', 'Cantonese'), ('Catalan', 'Catalan'), ('Cebuano', 'Cebuano'), ('Central Bicolano', 'Central Bicolano'), ('Chechen', 'Chechen'), ('Chinese', 'Chinese'), ('Chuvash', 'Chuvash'), ('Classical Chinese', 'Classical Chinese'), ('Crimean Tatar', 'Crimean Tatar'), ('Croatian', 'Croatian'), ('Czech', 'Czech'), ('Danish', 'Danish'), ('Dutch', 'Dutch'), ('Egyptian Arabic', 'Egyptian Arabic'), ('Emilian-Romagnol', 'Emilian-Romagnol'), ('English', 'English'), ('Esperanto', 'Esperanto'), ('Estonian', 'Estonian'), ('Faroese', 'Faroese'), ('Finnish', 'Finnish'), ('French', 'French'), ('Galician', 'Galician'), ('Georgian', 'Georgian'), ('German', 'German'), ('Gorontalo', 'Gorontalo'), ('Greek', 'Greek'), ('Gujarati', 'Gujarati'), ('Haitian', 'Haitian'), ('Hausa', 'Hausa'), ('Hebrew', 'Hebrew'), ('Hill Mari', 'Hill Mari'), ('Hindi', 'Hindi'), ('Hungarian', 'Hungarian'), ('Icelandic', 'Icelandic'), ('Ido', 'Ido'), ('Ilokano', 'Ilokano'), ('Indonesian', 'Indonesian'), ('Interlingua', 'Interlingua'), ('Irish', 'Irish'), ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Javanese', 'Javanese'), ('Kannada', 'Kannada'), ('Kazakh', 'Kazakh'), ('Kirghiz', 'Kirghiz'), ('Korean', 'Korean'), ('Kotava', 'Kotava'), ('Kurdish', 'Kurdish'), ('Latin', 'Latin'), ('Latvian', 'Latvian'), ('Ligurian', 'Ligurian'), ('Limburgish', 'Limburgish'), ('Lithuanian', 'Lithuanian'), ('Lombard', 'Lombard'), ('Low Saxon', 'Low Saxon'), ('Luxembourgish', 'Luxembourgish'), ('Macedonian', 'Macedonian'), ('Maithili', 'Maithili'), ('Malagasy', 'Malagasy'), ('Malay', 'Malay'), ('Malayalam', 'Malayalam'), ('Marathi', 'Marathi'), ('Mazandarani', 'Mazandarani'), ('Meadow Mari', 'Meadow Mari'), ('Min Dong', 'Min Dong'), ('Min Nan', 'Min Nan'), ('Minangkabau', 'Minangkabau'), ('Mingrelian', 'Mingrelian'), ('Mongolian', 'Mongolian'), ('Navajo', 'Navajo'), ('Neapolitan', 'Neapolitan'), ('Nepali', 'Nepali'), ('Newar', 'Newar'), ('North Frisian', 'North Frisian'), ('Norwegian', 'Norwegian'), ('Occitan', 'Occitan'), ('Oriya', 'Oriya'), ('Ossetian', 'Ossetian'), ('Pashto', 'Pashto'), ('Persian', 'Persian'), ('Piedmontese', 'Piedmontese'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Punjabi', 'Punjabi'), ('Quechua', 'Quechua'), ('Romanian', 'Romanian'), ('Russian', 'Russian'), ('Sakha', 'Sakha'), ('Samogitian', 'Samogitian'), ('Sanskrit', 'Sanskrit'), ('Scots', 'Scots'), ('Scottish Gaelic', 'Scottish Gaelic'), ('Serbian', 'Serbian'), ('Serbo-Croatian', 'Serbo-Croatian'), ('Sicilian', 'Sicilian'), ('Silesian', 'Silesian'), ('Sindhi', 'Sindhi'), ('Sinhalese', 'Sinhalese'), ('Slovak', 'Slovak'), ('Slovenian', 'Slovenian'), ('Sorani', 'Sorani'), ('South Azerbaijani', 'South Azerbaijani'), ('Spanish', 'Spanish'), ('Sundanese', 'Sundanese'), ('Swahili', 'Swahili'), ('Swedish', 'Swedish'), ('Tagalog', 'Tagalog'), ('Tajik', 'Tajik'), ('Tamil', 'Tamil'), ('Tatar', 'Tatar'), ('Telugu', 'Telugu'), ('Thai', 'Thai'), ('Turkish', 'Turkish'), ('Ukrainian', 'Ukrainian'), ('Upper Sorbian', 'Upper Sorbian'), ('Urdu', 'Urdu'), ('Uzbek', 'Uzbek'), ('Venetian', 'Venetian'), ('Vietnamese', 'Vietnamese'), ('Volapük', 'Volapük'), ('Walloon', 'Walloon'), ('Waray-Waray', 'Waray-Waray'), ('Welsh', 'Welsh'), ('West Frisian', 'West Frisian'), ('Western Punjabi', 'Western Punjabi'), ('Wu', 'Wu'), ('Yiddish', 'Yiddish'), ('Yoruba', 'Yoruba'), ('Zazaki', 'Zazaki')], max_length=50),
        ),
    ]