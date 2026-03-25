import sys
sys.path.insert(0, '.')

try:
    from system_wolin.multi_tables_query.api import multi_tables_query_app
    print('Multi_tables_query module import successful')
    print(f'Routes: {len(multi_tables_query_app.routes)}')
except Exception as e:
    print(f'Import failed: {str(e)}')
    import traceback
    traceback.print_exc()

try:
    from system_wolin.ai.api import ai_app
    print('AI module import successful')
    print(f'Routes: {len(ai_app.routes)}')
except Exception as e:
    print(f'AI Import failed: {str(e)}')
    import traceback
    traceback.print_exc()
