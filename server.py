from mcp.server.mcpserver import MCPServer

mcp = MCPServer("meal-helper")

@mcp.tool()
def get_meal_idea(ingredients: str, meal_type: str) -> str:
    return f"For {meal_type}, you can make something using: {ingredients}"