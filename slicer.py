if __name__ == '__main__':
    my_string = 'yooooouuuuupppppaaaaaaaasssssssee'
    currrent_slice = my_string.replace('oooo', '')
    currrent_slicea = currrent_slice.replace('uuuu', '')
    currrent_sliceb = currrent_slicea.replace('pppp', '')
    currrent_slicec = currrent_sliceb.replace('aaaaaaa', '')
    currrent_sliced = currrent_slicec.replace('sssss', '')
    currrent_slicef = currrent_sliced.replace('e', '')
    currrent_slicef = currrent_slicef.capitalize()
    print(currrent_slicef)
