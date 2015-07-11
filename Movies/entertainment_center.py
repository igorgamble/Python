import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)
avatar = media.Movie ("Avatar",
                      "A marine on an alien planet",
                      "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                      "https://youtu.be/5PSNL1qE6VY")
#print (avatar.storyline)
#avatar.show_trailer()
transformers = media.Movie ("Transformers","Optimus Prime, leader of the Autobots, narrates the collapse of the Transformers' home world, Cybertron",
                      "https://upload.wikimedia.org/wikipedia/ru/thumb/2/25/Transformers_Poster2rus.jpg/250px-Transformers_Poster2rus.jpg",
                      "https://youtu.be/dnD_Ar0P9dg")
#print (transformers.storyline)
#transformers.show_trailer()
school_of_rock = media.Movie ("School of Rock","A rock band known as No Vacancy performs at a nightclub two weeks before auditioning for an upcoming concert known as \"Battle of the Bands\".",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                              "https://youtu.be/LqEszt5wG9I")
#print (school_of_rock.storyline)
#school_of_rock.show_trailer()
dark_places = media.Movie ("Dark places","Set in a farming town in Kansas, Dark Places follows Libby Day (Charlize Theron), the only surviving witness of a horrific massacre that took her mother and sisters.",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/5/57/Dark_Places_2015_poster.jpg/220px-Dark_Places_2015_poster.jpg",
                              "https://youtu.be/SpG5dWV7piw")
#print (dark_places.storyline)
#dark_places.show_trailer()
the_hunger_games = media.Movie ("The Hunger Games","The dystopian nation of Panem consists of a wealthy, glamorous Capitol, ruled by President Snow, ruling twelve poorer districts.",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",
                              "https://youtu.be/KmYNkasYthg")
movies = [toy_story, avatar, transformers, school_of_rock, dark_places, the_hunger_games]
fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
#print (media.Movie.__doc__)
#print (media.Movie.__name__)
#print (media.Movie.__module__)
