from . import web


@web.route('/user', methods=['POST'])
def create_user():
    # 注册一个新用户
    pass

@web.route('/user<int:id>', methods=['GET'])
def get_user():
    # 返回一个用户
    pass

@web.route('/user<int:id>', methods=['DELETE'])
def delete_user():
    # 删除一个用户
    pass

@web.route('/user<int:id>', methods=['PUT'])
def update_user():
    # 修改一个用户
    pass

@web.route('/user', methods=['GET'])
def get_users():
    # 返回所有用户的集合
    pass