from user.serializer.user import CreateUserMemberSerializer


class CreateUserMemberHelper:

    def __init__(self , instance , validated_data):
        self.instance = instance 
        self.validated_data = validated_data

    def create_user(self):
            user_data = self.validated_data['user']
            user_data['first_name'] = self.instance.first_name
            user_data['last_name'] = self.instance.last_name
            user_data['school'] = self.instance.school
            serializer = CreateUserMemberSerializer(data = user_data)
            user = serializer.create(user_data)
            return user