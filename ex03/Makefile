# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hhasni <hhasni@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/07/01 15:42:06 by hhasni            #+#    #+#              #
#    Updated: 2015/07/01 15:42:10 by hhasni           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME 		=			Sully

SRC 		=			Sully.c

FILES		= 			Sully_0.c \
						Sully_0 \
						Sully_1.c \
						Sully_1 \
						Sully_2.c \
						Sully_2 \
						Sully_3.c \
						Sully_3 \
						Sully_4.c \
						Sully_4 \
						Sully_5.c \
						Sully_5


OBJ			= 			$(SRC:.c=.o)

CC 			= 			clang

CFLAGS 		=			-Wall -Wextra -Werror

RM 			= 			rm -rf

all: $(NAME)


$(NAME):
		@echo "\n\r\033[38;5;11m⌛  MAKE $(NAME) plz wait...\033[0m\033[K"
		@$(CC) $(CFLAGS) -o $(NAME) $(SRC)
		@echo -en "\r\033[38;5;22m✅  MAKE $(NAME)\033[0m\033[K"

clean: 
		@$(RM) $(FILES)
		@echo -en "\r\033[38;5;124m❌  CLEAN $(FILES)\033[0m\033[K"

fclean: clean
		@$(RM) $(NAME)
		@echo -en "\r\033[38;5;124m❌  FCLEAN $(NAME)\033[0m\033[K"

re: fclean all
