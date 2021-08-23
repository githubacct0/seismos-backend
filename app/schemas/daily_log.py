from marshmallow import Schema, fields


class DailyLogSchema(Schema):
    data = fields.Str(required=True, description="Some data about daily log")


class DailyLogData(Schema):
    date = fields.Int()
    description = fields.Str()


class DailyLogCreateSchema(Schema):
    project_id = fields.Int()
    well_id = fields.Int()
    logs = fields.List(fields.Nested(DailyLogData))


class DailyLogCreateResponseSchema(Schema):
    status = fields.Int()
    message = fields.Str()


class DailyLogResponseSchema(Schema):
    message = fields.Str()
    logs = fields.List(fields.Nested(DailyLogData))


class DailyLogRequestSchema(Schema):
    project_id = fields.Int()
    well_id = fields.Int()
