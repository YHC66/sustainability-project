# sustainability/views.py
import json
import os
from datetime import datetime
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import SustainabilityActionSerializer

class SustainabilityActionViewSet(viewsets.ViewSet):
    JSON_FILE_PATH = 'sustainability_actions.json'

    def get_data(self):
        # Create file if it doesn't exist
        if not os.path.exists(self.JSON_FILE_PATH):
            with open(self.JSON_FILE_PATH, 'w') as file:
                json.dump([], file)
            return []
        
        try:
            with open(self.JSON_FILE_PATH, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def save_data(self, data):
        with open(self.JSON_FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)

    def list(self, request):
        # GET /api/actions/
        data = self.get_data()
        return Response(data)

    def create(self, request):
        # POST /api/actions/
        serializer = SustainabilityActionSerializer(data=request.data)
        if serializer.is_valid():
            data = self.get_data()
            new_id = max([item['id'] for item in data], default=0) + 1
            new_action = {
                'id': new_id,
                'action': serializer.validated_data['action'],
                'date': serializer.validated_data['date'].strftime('%Y-%m-%d'),
                'points': serializer.validated_data['points']
            }
            data.append(new_action)
            self.save_data(data)
            return Response(new_action, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # GET /api/actions/<id>/
        data = self.get_data()
        try:
            action = next((item for item in data if item['id'] == int(pk)), None)
            if action:
                return Response(action)
            return Response(
                {"detail": "Action not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except (ValueError, TypeError):
            return Response(
                {"detail": "Invalid ID format"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk=None):
        # PUT /api/actions/<id>/
        try:
            data = self.get_data()
            action_index = next((index for index, item in enumerate(data) 
                               if item['id'] == int(pk)), None)
            
            if action_index is None:
                return Response(
                    {"detail": "Action not found"}, 
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = SustainabilityActionSerializer(data=request.data)
            if serializer.is_valid():
                updated_action = {
                    'id': int(pk),
                    'action': serializer.validated_data['action'],
                    'date': serializer.validated_data['date'].strftime('%Y-%m-%d'),
                    'points': serializer.validated_data['points']
                }
                data[action_index] = updated_action
                self.save_data(data)
                return Response(updated_action)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except (ValueError, TypeError):
            return Response(
                {"detail": "Invalid ID format"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, pk=None):
        # DELETE /api/actions/<id>/
        try:
            data = self.get_data()
            action_index = next((index for index, item in enumerate(data) 
                               if item['id'] == int(pk)), None)
            
            if action_index is None:
                return Response(
                    {"detail": "Action not found"}, 
                    status=status.HTTP_404_NOT_FOUND
                )

            data.pop(action_index)
            self.save_data(data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except (ValueError, TypeError):
            return Response(
                {"detail": "Invalid ID format"}, 
                status=status.HTTP_400_BAD_REQUEST
            )