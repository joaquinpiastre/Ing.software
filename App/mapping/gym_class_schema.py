from marshmallow import Schema, fields

class GymClassSchema(Schema):
    id = fields.Int(dump_only=True)
    gym_name = fields.Str(required=True)
    instructors_id= fields.Nested('InstructorSchema', many=True, exclude=('gym_classes',))