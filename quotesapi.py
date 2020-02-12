#imports the click module used to parse the command line
import click  
#imports the request (node.js feature) to get the API from web         
import requests

"""
A CLI application using REST API from Quotes API to generate quotes with the Python requests library to request the API for data
"""

@click.command()

#cli is the main function in program
def cli():

#function that makes a graphical introductory box
    draw_header()

#asks the user for name and introduces them to the program    
    greeting()    

#print a line to show separation
    click.echo('*' * 200)

#gets the info from Quotes API and the link is changed according to the choice made by the user
    quotes_request = requests.get(
        "http://quotes.rest/qod.json?category=" + choices())

#we take the data in json type into a dictionary called main_dict    
    main_dict = quotes_request.json()

#contents is the key in main and itself it is a dictionary    
    contents_dict = main_dict['contents'] 

#quotes is a list and quote is the dictionary under it. The below line prints the value of quote
    click.echo(click.style(contents_dict['quotes'][0]['quote'],fg = 'blue'))
    click.echo('::' * 100)





#function declaration
def choices():
    click.echo('Enter the preferences for the types of Quotes you would like')
    category=input("Which category would you like amongst: inspire,management,sports,life,funny,love,art,students")
    return category           


#function declaration
def draw_header():
    click.echo('\n')
    click.echo(click.style('*' * 100, fg='red'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='red'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='red'))
    click.echo(click.style('*' + ' ' * 32 + 'WELCOME TO THE Quotes Generator ' + ' ' * 32 + '*', fg='green'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='red'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='red'))
    click.echo(click.style('*' * 100, fg='red'))
    click.echo('\n')


#function declaration
def greeting():
    user_name = input('> What\'s your name?: ')
    print('\nWe are happy to have you with us {}, simply follow the following steps to get a quote according to your choice \n'.format(user_name))


#calls the cli() and the program starts
if __name__ == '__main__':
    cli()            
