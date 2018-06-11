# def most_frequent(data: list) -> str:
    # """
        # determines the most frequently occurring string in the sequence.
    # """
    # strings = []
    # values = []
    
    # for i in range(len(data)):
        # if data[i] in strings:
           # values[strings.index(data[i])] += 1

        # else:
            # strings.append(data[i])
            # values.append(1)
    
    # output = values.index(max(values))
    # final_output = strings[output]
    
    # return final_output

def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """

    return max(data, key=data.count)



print(most_frequent(['a', 'be', 'c', 'a', 'be', 'a', 'be', 'be']))

# if __name__ == '__main__':
    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # print('Example:')
    # print(most_frequent([
        # 'a', 'b', 'c', 
        # 'a', 'b',
        # 'a'
    # ]))
    
    # assert most_frequent([
        # 'a', 'b', 'c', 
        # 'a', 'b',
        # 'a'
    # ]) == 'a'

    # assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    # print('Done')
