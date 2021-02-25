def log(sequence, message,*values):
    if not values:
        print('%s: %s'%(sequence,message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s'%(sequence, message, values_str))

log(1, 'Favorites', 7, 33)
log('Favorite numbers', 7, 33)

