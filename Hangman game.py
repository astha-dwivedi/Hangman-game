import random;
print("WELCOME TO HANGMAN GAME");
print("you have 10 chances to guess a word if you can not guess than you loose");
n = 10
words_list = ['network', 'database', 'compiler', 'interpretor', 'anaconda', 'atom', 'sublime', 'jupyter', 'python', 'array', 'graph', 'graphics', 'testing', 'linker', 'loader'];
word = random.choice(words_list);
l = len(word);
print('_ '*l);
guessMade = "";
while (l>0 or n>0):
    main = "";
    guess = input();
    guessMade += guess;
    if guess in word:
        for letter in word:
            if letter in guessMade:
                main = main + letter+" ";
            else:
                main = main + "_ ";
        c = word.count(guess);
        l = l - c;
        print(main);
        if l==0:
            print("YOU WIN");
            print("YIPPIE..... YOU SAVE THE MAN");
            break;
    else:
        n -= 1;
        print("you have {} chances left".format(n));
        if n==9:
            print("---------");
        elif n==8:
            print("---------|");
            print("         |");
            print("         |");
            print("         |");
            print("         |");
            print("         |");
        elif n==7:
            print("---------|");
            print(" O       |");
            print("         |");
            print("         |");
            print("         |");
            print("         |");
        elif n==6:
            print("---------|");
            print(" O       |");
            print(" |       |");
            print("         |");
            print("         |");
            print("         |");
        elif n==5:
            print("---------|");
            print(" O       |");
            print(" |\      |");
            print("         |");
            print("         |");
            print("         |");
        elif n==4:
            print("---------|");
            print(" O       |");
            print("/|\      |");
            print("         |");
            print("         |");
            print("         |");
        elif n==3:
            print("---------|");
            print(" O       |");
            print("/|\      |");
            print("  \      |");
            print("         |");
            print("         |");
        elif n==2:
            print("---------|");
            print(" O       |");
            print("/|\      |");
            print("/ \      |");
            print("         |");
            print("         |");
        elif n==1:
            print("-|-------|");
            print(" O       |");
            print("/|\      |");
            print("/ \      |");
            print("         |");
            print("         |");
        else:
            print("YOU LOOSE AND GOSH!! MAN IS HANGED");
            break;
        
    
        