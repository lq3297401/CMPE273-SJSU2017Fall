'''
################################## client.py #############################
# Wallet Client calls a remote GRPC service to encrypt credit/debit cards
# data and decrypt token back to plain text card detail.
################################## client.py #############################
'''
import grpc
import wallet_pb2

class WalletClient(object):
    '''
    WalletClient encrypts and decrypts card info via GRPC's sub which internally calls
    the remote WalletServicer.
    '''

    def __init__(self, host='0.0.0.0', port=3000):
        '''
        Initializes GRPC channel and stud so that they can be used in encrypt and decrypt functions.
        '''
        # TODO
        #%s,表示格化式一个对象为字符, %d,整数, exp: "%s:%d"%("ab",3) => "ab:3"
        self.channel = grpc.insecure_channel('%s:%d' % (host, port) )
        self.stub = wallet_pb2.WalletStub(self.channel)


    def encrypt(self, plain_text):
        '''
        Encrypts raw card info via stub.
        :param self: the self reference
        :param plain_text: the card details in a dictionary, E.g. plain_text['card_holder_name']
            converts from plain_text => wallet_pb2.Card => wallet_pb2.CardEncryptRequest
        :return: return a protocol buffer card encrypted response.
        :rtype: wallet_pb2.CardEncryptResponse
        '''
        # TODO
        #from wallet.proto, we know that return type is wallet_pb2.CardEncryptResponse,
        #so we need wallet_pb2.CardEncryptRequest. and we need a Card mycard to generates
        #all these information.
        # all the request and response function are from wallet_pb2. So don't forget to write
        # the function with classname like: wallet_pb2.request  wallet_pb2.response
            #initial card first
          mycard =  wallet_pb2.Card{
          card_holder_name = plain_text['card_holder_name']
          card_number = plain_text['card_number']
          card_expiry_yyyymm = plain_text['card_expiry_yyyymm']
        }
            #generate CardEncryptRequest, from .proto we know the parameter for CardEncryptRequest() is card.
        request1 = wallet_pb2.CardEncryptRequest(card = mycard)
            #generate return from CardEncryptRequest
        return wallet_pb2.CardEncryptResponse(request1)

    def decrypt(self, _token):
        '''
        Decrypts _token via stub.
        :param self: the self reference
        :param _token: the encrypted token
        :return: return a protocol buffer card decrypted response.
        :rtype: wallet_pb2.CardDecryptResponse
        '''
        # TODO
        #from wallet.proto, we know that return type is wallet_pb2.CardDecryptResponse,
        #and the final return is a decrypted response, so we need the decrypted() function of server
        #so we need wallet_pb2.CardDecryptRequest. als from .proto we know that
        #the parameter of CardDecryptRequest() is tocken
        request2 = wallet_pb2.CardDecryptRequest(token = _token)
        # client first call stub(proto)
        return self.stub.decrypt(request2)
