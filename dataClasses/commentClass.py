# Create a simple "" comment class which will have am "id" & "text" as integer & string accordingly.


class Comment():
    def __init__(self, id: int, text: str):
        self.id = id
        self.text = text
    
    # By using this "__repr__" method, will display the class-variables by printing the class-instance only.
    def __repr__(self):
        return f"ID: {self.id} --- Text: {self.text}"
    

    # check the instance of this class "Comment" based on the "text" attribute
    def __eq__(self, other):
        return self.text == other.text


commentObj1 = Comment( 1, "text comment" )
commentObj2 = Comment( 2, "text comment" )


print( commentObj1 ) # the "__repr__" method of the class "Comment" helps to print the variable.


# comapare the two instance of the class "Comment"
print( commentObj1 is commentObj2)
print( commentObj1 == commentObj2)


