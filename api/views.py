from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import models 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
User = get_user_model()

#        user = request.user
#        data = request.data
#        data = request.query_params 



class testing(APIView):
    def get(self,request):
        data = models.PostTable.objects.all()
        serializer = serializers.PostTableSerializer(data, many=True)
        return Response(serializer.data)

    
    def post(self,request):
        error = False
        data = request.data
        user = User.objects.create_user(username=data["username"],password=data["password"])
        Token.objects.create(user=user)
        return Response({'error':error})
    
    def delete(self,request):
        error = False
        return Response({'error':error})


class Register(APIView):
    def post(self,request):
        error = False
        try:
            data = request.data
            user = User.objects.create_user(username=data["username"],password=data["password"])
            Token.objects.create(user=user)
        except:
            error = True
        return Response({'error':error})
    
class GET_user(APIView):
    def get(self,request):
        user = request.user
        #user = User.objects.get(username = "VidyaSagar")
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)
        
            
            
class LST_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    
    def get(self,request):
        error = False
        try:
            data = models.Lost_Found.objects.all()
            serializer = serializers.Lost_FoundSerializer(data, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({"error":error})

    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            lst = models.Lost_Found()
            lst.username = user
            lst.title = data['title']
            lst.description = data['description']
            lst.img = data['img']
            lst.save()
        except:
            error = True
        return Response({'error':error}) 
    
    def delete(self,request):
        error = False
        try:
            data = request.query_params
            lst = models.Lost_Found.objects.get(id = data['lst_id'])
            lst.delete()
        except:
            error = True
        return Response({'error':error})
    

class LST_Comment_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    
    def get(self,request):
        error = False
        try:
            data = request.query_params 
            #LST_list = models.Lost_Found.objects.get(title = "Lost my soulmate")       
            LST_list = models.Lost_Found.objects.get(id = data['lst_id'])
            comments = LST_list.lst_found_comment.all()
            serializer = serializers.LST_CommentsSerializer(comments,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({"error":error})
    
    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            LST_list = models.Lost_Found.objects.get(lst_id = data['id'])
            new_comment = models.LST_Comments()
            new_comment.lst_cmnt_id = LST_list
            new_comment.Comment = data['comment']
            new_comment.username = user.username
            new_comment.save()
        except:
            error = True
        return Response({'error':error})
    
    
    def delete(self,request):
        error =  False
        try:
            data = request.query_params
            comment_list = models.LST_Comments.objects.get(id = data['lst_cmnt_id'])  # id is primary key of comments
            comment_list.delete()
            lst = models.Lost_Found.objects.get(id = data['lst_id'])
            lst.comment_count -= 1
            lst.save()
        except:
            error = True
        return Response({'error':error})
     
class POST_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    
    def get(self,request):
        error = False
        try:
            #user = User.objects.get(username = "srinivas")
            user = request.user
            post_list = models.PostTable.objects.all()
            for i in post_list:
                try:
                    like = models.post_Likes.objects.get(post_id = i,username = user)
                    i.is_like = True
                except:
                    i.is_like = False
            serializer = serializers.PostTableSerializer(post_list,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})
        
    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            post = models.PostTable()
            post.username = user
            post.title = data['title']
            post.description = data['description']
            post.img = data['img']
            post.save()
        except:
            error = True
        return Response({'error':error})
    
    def delete(self,request):
        error = False
        try:
            data = request.query_params
            post = models.PostTable.objects.get(id = data['post_id'])
            post.delete()
        except:
            error = True
        return Response({'error':error})    
            

class PST_CMNT_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    
    def get(self,request):
        error = False
        try:
            data = request.query_params 
            #post = models.PostTable.objects.get(id = "1")
            post = models.PostTable.objects.get(id = data['post_id'])
            pst_comments = models.post_Comments.objects.filter(post_id = post)
            serializer = serializers.post_CommentsSerializer(pst_comments,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})
    
    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            post_cmnt = models.post_Comments()
            post_cmnt.post_id = models.PostTable.objects.get(post_id = data['id'])
            post_cmnt.username = user
            post_cmnt.Comment = data['comment']
            post_cmnt.save()
        except:
            error = True
        return Response({'error':error})
            
    def delete(self,request):
        error = False
        try:
            data = request.query_params
            post_cmnt = models.post_Comments.objects.get(id = data['cmnt_id'])
            post_cmnt.delete()
            post = models.PostTable.objects.get(id = data['post_id'])
            post.comment_count -= 1
            post.save()
        except:
            error = True
        return Response({'error':error})
    
class POST_LIKE_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    
    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            post = models.PostTable.objects.get(post_id = data['post_id'])
            post.like_count += 1
            post.save()
            post_like = models.post_Likes()
            post_like.username = user
            post_like. post_id = post
            post_like.save()
        except:
            error = True
        return Response({'error':error})
    
    def delete(self,request):
        error = False
        try:
            data = request.query_params
            post = models.PostTable.objects.get(id = data['post_id'])
            post.like_count -= 1
            post.save()
            like = models.post_Likes.objects.get(post_id = post)
            like.delete()
        except:
            error = True
        return Response({'error':error})
            
        
class EVENT_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    
    def get(self,request):
        error = False
        try:
            user = request.user
            #user = User.objects.get(id = "1")
            event_list = models.Events.objects.all()
            for i in event_list:
                try:
                    like = models.Event_likes.objects.get(event_id = i,username = user)
                    i.is_like = True
                except:
                    i.is_like = False
            serializer = serializers.EventsSerializer(event_list,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})
    
    
    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            event = models.Events()
            event.username = user
            event.title = data['title']
            event.description = data['description']
            event.event_img = data['img']
            event.event_vedio = data['vedio']
            event.save()
            
        except:
            error = True
        return Response({'error':error})
    
    def delete(self,request):
        error = False
        try:
            data = request.query_params
            event = models.Events.objects.get(id = data['event_id'])
            event.delete()
        except:
            error = True
        return Response({'error':error})

class EVENT_LIKE_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    
    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            event = models.Events.objects.get(event_id = data['id'])
            event_like = models.Event_likes()
            event_like.username = user
            event_like.event_id = event
            event_like.save()
        except:
            error = True
        return Response({'error':error})
    
    def delete(self,request):
        error = False
        try:
            data = request.query_params
            like = models.Event_likes.objects.get(id = data['id'])
            like.delete()
        except:
            error = True
        return Response({'error':error})


class ALERT_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
   
    def get(self,request):
        error = False
        try:     
            data = models.Alerts.objects.all()
            serializer = serializers.AlertsSerializer(data, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})
    
    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            alert = models.Alerts()
            alert.username = user
            alert.title = data['title']
            alert.description = data['description']
            alert.img = data['img']
            alert.save()
        except:
            error = True
        return Response({'error':error})
    
    def delete(self,request):
        error = False
        try:
            data = request.query_params
            alert = models.Alerts.objects.get(id = data['alert_id'])
            alert.delete()
        except:
            error = True
        return Response({'error':error})

class CLUB_SPORT_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    
    def get(self,request):
        error = False
        try:
            data = request.query_params   
            #clubs_sports = models.Clubs_Sports.objects.filter(club_r_sport = 'sport')     
            clubs_sports = models.Clubs_Sports.objects.filter(club_r_sport = data['club_sport'])
            serializer = serializers.Clubs_SportsSerializer(clubs_sports,many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})
    
    def post(self,request):
        error = False
        try:
            data = request.data
            club_r_sport = models.Clubs_Sports()
            club_r_sport.logo = data['img']
            club_r_sport.title = data['title']
            club_r_sport.club_r_sport = data['club_r_sport']
            club_r_sport.username = data['name']
            head = User.objects.get(username = data['head'])
            club_r_sport.head = head
            club_r_sport.team_members = data['team_members']
            club_r_sport.websites = data['websites']
            club_r_sport.save()
        except:
            error = True
        return Response({'error':error})
        



class CLUB_SPORT_MEMB(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    
    def get(self,request):
        error = False
        try:
            data = request.query_params               
            club_mem = data["team_mem"].split('@')
            club_mem_data = []
            for i in club_mem:
                try:
                    user = User.objects.get(username = i)
                    club_mem_data.append(user)
                except:
                    continue
            #user = User.objects.get(username = data['club_name'])
            #user = User.objects.get(username = "cricket")
            #club_files = user.post_table_username.all()
            serializer = serializers.UserSerializer(club_mem_data, many=True)
            
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})
    
    def post(self,request):
        error = False
        try:
            data = request.data              
            user = User.objects.get(username = data['club_sport'])
            #user = User.objects.get(username = "cricket")
            club_files = user.post_table_username.all()
            serializer = serializers.PostTableSerializer(club_files, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})


class PEOFILE_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    
    def get(self,request):
        error = False
        try:
            user = request.user  
            #user = User.objects.get(id = "1")  
            data = user.post_table_username.all()    
            serializer = serializers.PostTableSerializer(data, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})
    
    

class SAC_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    
    def get(self,request):
        error = False
        try:
            data = User.objects.filter(is_sac = True)
            serializer = serializers.UserSerializer(data, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})
            



class MESS_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    
    def get(self,requesr):
        error = False
        try:   
            mess = models.Mess_table.objects.all()     
            serializer = serializers.Mess_tableSerializer(mess,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})
    
    
    
    
    
class ACADEMIC_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    
    def get(self,requesr):
        error = False
        try:   
            academic = models.Academic_table.objects.all()       
            serializer = serializers.Academic_tableSerializer(academic,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})
    

class TIMETABLE_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    
    def get(self,requesr):
        error = False
        try:   
            timetable = models.Time_table.objects.all()       
            serializer = serializers.Time_tableSerializer(timetable,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})







    
