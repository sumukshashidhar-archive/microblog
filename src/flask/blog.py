from app import app


@app.route('/getAllPosts', methods=['GET'])
def get_all_posts():
    """
    A method for getting all the posts of a particular user
    :return: Array
    """
    