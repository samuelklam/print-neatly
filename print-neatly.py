import math

class Print_Neatly(object):

    def print_neatly(self, words, n, M):
        """
        Function prints a paragraph neatly
        @param words : an array of words
        @param n : number of words in the array
        @param M : maximum line length
        """
        minpenalty = [float('inf')]*(n+1)
        break_points = [None]*(n+1)

        # intialize base case
        minpenalty[0] = 0

        def compute_line_cost(extra_space, j, n):
            # handle the 3 cases described in the prompt
            if extra_space < 0:
                return float('inf')
            elif j == n and extra_space >= 0:
                return 0
            else:
                return extra_space**3

        for j in range(1, n+1):
            extra_space = M + 1
            for i in range(j, int(max(1, j + 1 - math.ceil(M/2)))-1, -1):
                extra_space = extra_space - len(words[i]) - 1
                cur_penalty = minpenalty[i-1] + compute_line_cost(extra_space, j, n)
                if minpenalty[j] > cur_penalty:
                    minpenalty[j] = cur_penalty
                    break_points[j] = i

        return minpenalty, break_points

    def print_neatly_non_optimized(self, words, n, M):
        """
        Non optimized print neatly runs in O(n^2) time and space
        """

        # note that this indexing follows the nomenclature of matrix indexing
        # to allow for compatability with the write up
        extraspace = linecost = [[None for i in range(n+1)] for j in range(n+1)]
        minpenalty = [float('inf')]*(n+1)
        pointer_list = [None]*(n+1)

        # intialize base case
        minpenalty[0] = 0

        # we first compute the extra spaces for words 1 through n
        for i in range(1, n+1):
            extraspace[i][i] = M - len(words[i])
            for j in range(i+1, n+1):
                # we get the extra space left and subtract that new word j plus the space between
                extraspace[i][j] = extraspace[i][j-1] - len(words[j]) - 1

        # we next compute the line cost for words 1 through n
        for i in range(1, n+1):
            for j in range(1, n+1):
                # we follow the 3 cases described in the writeup
                if extraspace[i][j] < 0:
                    linecost[i][j] = float('inf')
                elif j == n and extraspace[i][j] >= 0:
                    linecost[i][j] = 0
                else:
                    linecost[i][j] = (extraspace[i][j])**3

        # we then compute the minimal penalty for each line
        for j in range(1, n+1):
            for i in range(1, j+1):
                cur_penalty = minpenalty[i-1] + linecost[i][j]
                if minpenalty[j] > cur_penalty:
                    minpenalty[j] = cur_penalty
                    pointer_list[j] = i

        return minpenalty, pointer_list

    def reconstruct_lines(self, text, j, break_points):
        i = break_points[j]
        line_num = 1
        if i != 1:
            line_num = self.reconstruct_lines(text, i-1, break_points) + 1
        print ' '.join(text[i:(j+1)])
        return line_num


text = "Buffy the Vampire Slayer fans are sure to get their fix with the DVD release of the show's first season. The three-disc collection includes all 12 episodes as well as many extras. There is a collection of interviews by the show's creator Joss Whedon in which he explains his inspiration for the show as well as comments on the various cast members. Much of the same material is covered in more depth with Whedon's commentary track for the show's first two episodes that make up the Buffy the Vampire Slayer pilot. The most interesting points of Whedon's commentary come from his explanation of the learning curve he encountered shifting from blockbuster films like Toy Story to a much lower-budget television series. The first disc also includes a short interview with David Boreanaz who plays the role of Angel. Other features include the script for the pilot episodes, a trailer, a large photo gallery of publicity shots and in-depth biographies of Whedon and several of the show's stars, including Sarah Michelle Gellar, Alyson Hannigan and Nicholas Brendon."

tests = [text]
print_neat = Print_Neatly()

for test in tests:
    test = ['BLANK'] + test.split(' ')
    n = len(test)-1
    M = 40
    min_p, p_list = print_neat.print_neatly(test, n, M)
    min_p2, p_list2 = print_neat.print_neatly_non_optimized(test, n, M)
    print_neat.reconstruct_lines(test, n, p_list)
    print_neat.reconstruct_lines(test, n, p_list2)
    print min_p[-1], min_p2[-1]
