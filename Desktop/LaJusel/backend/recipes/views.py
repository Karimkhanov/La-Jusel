from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Recipe, Category
from .serializers import RecipeSerializer, CategorySerializer


# Create
class RecipeCreateAPIView(APIView):
    def post(self, request):
        try:
            category = Category.objects.get(pk=request.data.get('category_id'))
        except Category.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category=category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Read - all list of recipes
class RecipeListAPIView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Read, Update, Delete The Recipe
class recipeDetailAPIView(APIView):
    def get(self, request, id):
        recipe = Recipe.objects.get(id=id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        recipe = Recipe.objects.get(id=id)
        serializer = RecipeSerializer(recipe, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        recipe = Recipe.objects.get(id=id)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# get category by his title
@api_view(['GET', 'PUT', 'DELETE'])
def getCategoryByName(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
