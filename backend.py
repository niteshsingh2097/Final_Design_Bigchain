

class back:

    def docreate(d1, d2, pubkey, prikey):
        from bigchaindb_driver import BigchainDB
        try:
            print(d1, d2)
            bdb = BigchainDB('https://test.ipdb.io/')

            tx = bdb.transactions.prepare(
                operation='CREATE',
                signers=pubkey,
                asset={'data': {
                    'car': {
                        'vehicle_number': d1,
                        'manufacturer': d2,
                    },
                }, })

            signed_tx = bdb.transactions.fulfill(
                tx, private_keys=prikey)
            bdb.transactions.send_commit(signed_tx)
            return signed_tx, prikey
        except:
            return "INVALID KEYS"

    def checker(id):
        from bigchaindb_driver import BigchainDB
        bdb = BigchainDB('https://test.ipdb.io/')

        block_height = bdb.blocks.get(txid=id)
        try:
            if bdb.blocks.retrieve(str(block_height)):
                return "sucess"
        except:
            return "failed or incorrect ID"

    def asset_transfer(txid, opk, rpk, oprk):
        try:
            from bigchaindb_driver import BigchainDB
            bdb = BigchainDB('https://test.ipdb.io/')
            creation_tx = bdb.transactions.retrieve(txid)
            asset_id = creation_tx['id']
            ownerPrivateKey = oprk
            ownerPublicKey = opk
            recepientPublicKey = rpk

            transfer_asset = {
                'id': asset_id,
            }

            output_index = 0

            output = creation_tx['outputs'][output_index]
            transfer_input = {
                'fulfillment': output['condition']['details'],
                'fulfills': {
                    'output_index': output_index,
                    'transaction_id': creation_tx['id'],
                },
                'owners_before': output['public_keys'],
            }
            prepared_transfer_tx = bdb.transactions.prepare(
                operation='TRANSFER',
                asset=transfer_asset,
                inputs=transfer_input,
                recipients=recepientPublicKey,
            )
            fulfilled_transfer_tx = bdb.transactions.fulfill(
                prepared_transfer_tx,
                private_keys=ownerPrivateKey,
            )
            return fulfilled_transfer_tx, ownerPrivateKey
        except:
            return "INVALID INPUT / INVALID KEYS"," "

    def queryer(srch):
        from bigchaindb_driver import BigchainDB
        bdb = BigchainDB('https://test.ipdb.io/')
        msg = bdb.assets.get(search=srch)
        if msg == []:
            return "Not Found"

        return msg

    """def checkerpoform(ID, pk):
        from bigchaindb_driver import BigchainDB
        bdb = BigchainDB('https://test.ipdb.io/')
        txid = ID
        public_key = pk
        output_index = 0
        creation_tx = bdb.transactions.retrieve(txid)
        output = creation_tx['outputs'][output_index]

        if output['public_keys'][0] == public_key:
            return "YES"
        else:
            return "NO"""

    def init():
        from bigchaindb_driver import BigchainDB
        from bigchaindb_driver.crypto import generate_keypair
        bdb = BigchainDB('https://test.ipdb.io/')
        alice = generate_keypair()
        return alice.public_key, alice.private_key
