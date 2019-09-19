async def test_status_responds_with_successfull_payload(test_client):
    response = await test_client.get('/api/status')
    data = await response.json()
    assert 'status' in data
    assert data['status'] == 'OK'
