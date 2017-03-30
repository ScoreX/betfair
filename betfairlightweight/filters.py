

class BaseFilter:
    """Base Filter"""


class MarketFilter(BaseFilter):

    def __init__(self, market_ids=None, bsp_only=None, market_betting_types=None, event_type_ids=None, event_ids=None,
                 turn_in_play_enabled=None, market_type_codes=None, venues=None, market_countries=None, text_query=None,
                 competition_ids=None, in_play_only=None, market_start_time=None, with_orders=None):
        self.text_query = text_query
        self.event_type_ids = event_type_ids or []
        self.event_ids = event_ids or []
        self.competition_ids = competition_ids or []
        self.market_ids = market_ids or []
        self.venues = venues or []
        self.bsp_only = bsp_only
        self.turn_in_play_enabled = turn_in_play_enabled
        self.in_play_only = in_play_only
        self.market_betting_types = market_betting_types or []
        self.market_type_codes = market_type_codes or []
        self.market_countries = market_countries or []
        self.market_start_time = market_start_time
        self.with_orders = with_orders or []

    @property
    def serialise(self):
        return {
            'marketIds': self.market_ids,
            'textQuery': self.text_query,
            'marketBettingTypes': self.market_betting_types,
            'eventTypeIds': self.event_type_ids,
            'eventIds': self.event_ids,
            'turnInPlayEnabled': self.turn_in_play_enabled,
            'inPlayOnly': self.in_play_only,
            'marketTypeCodes': self.market_type_codes,
            'venues': self.venues,
            'marketCountries': self.market_countries,
            'bspOnly': self.bsp_only,
            'competitionIds': self.competition_ids,
            'marketStartTime': self.market_start_time,
            'withOrders': self.with_orders,
        }


class StreamingMarketFilter(BaseFilter):

    def __init__(self, market_ids=None, bsp_market=None, betting_types=None, event_type_ids=None, event_ids=None,
                 turn_in_play_enabled=None, market_types=None, venues=None, country_codes=None):
        self.market_ids = market_ids or []
        self.bsp_market = bsp_market
        self.betting_types = betting_types or []
        self.event_type_ids = event_type_ids or []
        self.event_ids = event_ids or []
        self.turn_in_play_enabled = turn_in_play_enabled
        self.market_types = market_types or []
        self.venues = venues or []
        self.country_codes = country_codes or []

    @property
    def serialise(self):
        return {
            'marketIds': self.market_ids,
            'bspMarket': self.bsp_market,
            'bettingTypes': self.betting_types,
            'eventTypeIds': self.event_type_ids,
            'eventIds': self.event_ids,
            'turnInPlayEnabled': self.turn_in_play_enabled,
            'marketTypes': self.market_types,
            'venues': self.venues,
            'countryCodes': self.country_codes,
        }


class StreamingMarketDataFilter(BaseFilter):

    def __init__(self, fields=None, ladder_levels=None):
        """
        fields: EX_BEST_OFFERS_DISP, EX_BEST_OFFERS, EX_ALL_OFFERS, EX_TRADED,
                EX_TRADED_VOL, EX_LTP, EX_MARKET_DEF, SP_TRADED, SP_PROJECTED
        ladder_levels: 1->10
        """
        self.fields = fields or []
        self.ladder_levels = ladder_levels

    @property
    def serialise(self):
        return {
            'fields': self.fields,
            'ladderLevels': self.ladder_levels
        }


def market_filter(textQuery=None, eventTypeIds=None, eventIds=None, competitionIds=None, marketIds=None, venues=None,
                  bspOnly=None, turnInPlayEnabled=None, inPlayOnly=None, marketBettingTypes=None, marketCountries=None,
                  marketTypeCodes=None, marketStartTime=None, withOrders=None):
    """
    Create filters to apply to market data we wish to receive.
    :param str textQuery: restrict markets by text associated with it, e.g name, event, comp.
    :param list eventTypeIds: filter market data to data pertaining to specific event_type ids.
    :param list eventIds: filter market data to data pertaining to specific event ids.
    :param list competitionIds: filter market data to data pertaining to specific competition ids.
    :param list marketIds: filter market data to data pertaining to specific marketIds.
    :param list venues: restrict markets by venue (only horse racing has venue at the moment)
    :param bool bspOnly: restriction on bsp, not supplied will return all.
    :param bool turnInPlayEnabled: restriction on whether market will turn in play or not, not supplied returns all.
    :param bool inPlayOnly: restriction to currently inplay, not supplied returns all.
    :param list marketBettingTypes: filter market data by market betting types.
    :param list marketCountries: filter market data by country codes.
    :param list marketTypeCodes: filter market data to match the type of market e.g. MATCH_ODDS.
    :param betfairlightweight.utils.create_timerange marketStartTime: filter market data by time at which it starts.
    :param betfairlightweight.enums.OrderStatus withOrders: filter market data by specified order status.
    :returns: filter dictionary to be applied to market data request.
    :rtype: dict
    """
    args = locals()
    return {
        k: v for k, v in args.items() if v is not None
    }
