import pytest


class TestEverything:
    async def check_client(self):
        try:
            _ = self.client
        except AttributeError:
            self.client = AmariClient(self.get_token())

    @pytest.mark.asyncio
    async def test_users(self):
        """Tests the fetching users function"""
        await self.check_client()

        await self.client.fetch_user(814233207515643974, 374147012599218176)
        await self.client.fetch_users(
            854118090173186058, ["854118090173186058", "107510319315697664", "249955383001481216"]
        )

    @pytest.mark.asyncio
    async def test_leaderboards(self):
        """Tests the fetching leaderboards function"""
        await self.check_client()

        await self.client.fetch_leaderboard(854118090173186058, page=3, limit=100)
        await self.client.fetch_full_leaderboard(854118090173186058, weekly=True)

    @pytest.mark.asyncio
    async def test_rewards(self):
        """Tests the fetching rewards function"""
        await self.check_client()

        await self.client.fetch_rewards(854118090173186058, page=1, limit=20)

    @pytest.mark.asyncio
    async def pytest_sessionfinish(self, session, exitstatus):
        """Closes the session at the end of the tests"""
        await self.client.close()

    def get_token(self):
        with open(__file__[:-15] + "amari_secret", "r") as secret:
            return secret.read()