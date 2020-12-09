from flask_restful import Resource, abort
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from helpers.validations import (validate_json_request, validate_uuid)
from schema.diary_schema import DiarySchema
from utils.handle_response import success_response, error_response
from models.diary_model import Diary as DiaryModel


class DairyResource(Resource):
    @jwt_required
    def get(self):
        user_diaries = DiaryModel.query.filter_by(
            user_id=get_jwt_identity().get('id'), deleted=False).all()
        return success_response(data=DiarySchema(many=True).dump(user_diaries),
                                status=200,
                                message='Diaries retrieved successfully')

    @jwt_required
    @validate_json_request(request)
    def post(self):
        diary_data = request.get_json(force=True)
        diary_data = DiarySchema(exclude=['id', 'created_on', 'updated_on']).\
            load_object_into_schema(diary_data)
        diary_data['user_id'] = get_jwt_identity().get('id')
        new_diary = DiaryModel(**diary_data).save()
        return success_response(data=DiarySchema().dump(new_diary),
                                status=201,
                                message='Your diary was successfully created')


class SingleDiaryResource(Resource):
    @jwt_required
    def get(self, diary_id):
        validate_uuid(diary_id)
        user_diary = DiaryModel.query.filter_by(
            id=diary_id, deleted=False,
            user_id=get_jwt_identity().get('id')).first()
        if not user_diary:
            return error_response(message='Diary not found', status=404)
        return success_response(data=DiarySchema().dump(user_diary),
                                status=200,
                                message='Diary retrieved successfully')

    @jwt_required
    @validate_json_request(request)
    def put(self, diary_id):
        validate_uuid(diary_id)
        diary_update_data = request.get_json(force=True)
        diary_data = DiarySchema(exclude=['id', 'created_on', 'updated_on']).\
            load_object_into_schema(
                diary_update_data, partial=True)
        user_diary = DiaryModel.query.filter_by(
            id=diary_id, deleted=False,
            user_id=get_jwt_identity().get('id')).first()
        if not user_diary:
            return error_response(message='Diary not found', status=404)
        if user_diary.updated_on and (
                user_diary.updated_on - user_diary.created_on).days > 0:
            return error_response(
                message='Diary cannot be modified after 24hrs', status=400)
        user_diary = user_diary.update(**diary_data)
        return success_response(data=DiarySchema().dump(user_diary),
                                status=200,
                                message='Diary updated successfully')

    @jwt_required
    def delete(self, diary_id):
        validate_uuid(diary_id)
        user_diary = DiaryModel.query.filter_by(
            id=diary_id, deleted=False,
            user_id=get_jwt_identity().get('id')).first()
        if not user_diary:
            return error_response(message='Diary not found', status=404)
        user_diary.delete()
        return success_response(message='Diary deleted successfully')
