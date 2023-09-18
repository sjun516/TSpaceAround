from flask import Blueprint, jsonify, request
import apps.service.project as card_history_analyze
import apps.service.get_temp as data_pop

bp = Blueprint(name='bp',
                       import_name=__name__,
                       url_prefix='/user')

@bp.route('/category', methods=['GET'])
def getCategoryWithUser():
    userName = request.args.get('name')
    categoryResult = card_history_analyze.card_history_analyze_category(userName)
    data = {
        'category': categoryResult
    }
    res = jsonify(data)
    return res

@bp.route('/myLifeStyle', methods=['GET'])
def getLifeStyleDataWithUser():
    userName = request.args.get('name')
    expenditure = card_history_analyze.card_history_analyze_expenditure(userName)
    ment = data_pop.getMentByUser(userName)
    storeName = data_pop.getStoreNameByUser(userName)
    data = {
        'ex': expenditure,
        'ment': ment,
        'store': storeName
    }
    res = jsonify(data)
    return res

@bp.route('/getStoreGps', methods=['GET'])
def getStoreGpsWithUser():
    userName = request.args.get('name')
    storeData = data_pop.getStoreGpsByUser(userName)
    res = jsonify(storeData)
    return res
