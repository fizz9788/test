import sys
sys.path.insert(0, '.')

try:
    from system_wolin.ai.api import ai_app
    print('✓ AI module import successful')
    print(f'✓ AI app routes: {len(ai_app.routes)}')
except Exception as e:
    print(f'✗ Import failed: {str(e)}')
    import traceback
    traceback.print_exc()
