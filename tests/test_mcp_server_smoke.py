"""Smoke tests for MCP server tool registration and handlers."""

import json

from ailawfirm_uk.mcp_server import TOOLS, handle_request


class TestMCPServerSmoke:
    def test_uk_court_lookup_registered(self):
        assert "uk_court_lookup" in TOOLS
        assert "query" in TOOLS["uk_court_lookup"]["input_schema"]["required"]

    def test_uk_citation_validator_registered(self):
        assert "uk_citation_validator" in TOOLS
        assert "citation" in TOOLS["uk_citation_validator"]["input_schema"]["required"]

    def test_uk_calendar_sync_registered(self):
        assert "uk_calendar_sync" in TOOLS
        req = TOOLS["uk_calendar_sync"]["input_schema"]["required"]
        assert "event_id" in req
        assert "start_iso" in req
        assert "end_iso" in req

    def test_mcp_initialize(self):
        response = handle_request({"method": "initialize", "params": {}, "id": 1})
        assert response is not None
        result = response["result"]
        assert result["serverInfo"]["name"] == "ailawfirm-uk"
        assert result["protocolVersion"] == "2024-11-05"

    def test_tools_list_includes_uk_tools(self):
        response = handle_request({"method": "tools/list", "params": {}, "id": 2})
        assert response is not None
        tool_names = [t["name"] for t in response["result"]["tools"]]
        assert "uk_court_lookup" in tool_names
        assert "uk_citation_validator" in tool_names
        assert "uk_calendar_sync" in tool_names

    def test_tools_call_uk_court_lookup(self):
        response = handle_request(
            {
                "method": "tools/call",
                "params": {"name": "uk_court_lookup", "arguments": {"query": "UKSC"}},
                "id": 3,
            }
        )
        assert response is not None
        content = json.loads(response["result"]["content"][0]["text"])
        assert content["status"] == "found"

    def test_tools_call_uk_citation_validator(self):
        response = handle_request(
            {
                "method": "tools/call",
                "params": {
                    "name": "uk_citation_validator",
                    "arguments": {"citation": "[2023] EWCA Civ 123"},
                },
                "id": 4,
            }
        )
        assert response is not None
        content = json.loads(response["result"]["content"][0]["text"])
        assert content["valid"] is True
        assert content["format"] == "OSCOLA_NEUTRAL"
