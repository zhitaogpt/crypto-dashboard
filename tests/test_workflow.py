import yaml
from pathlib import Path

def test_cache_workflow_structure():
    wf_path = Path('.github/workflows/cache.yml')
    assert wf_path.exists(), 'cache workflow file missing'
    data = yaml.safe_load(wf_path.read_text())
    assert data.get('name') == 'Cache crypto data (no-key NVT & valuation basket)'
    jobs = data.get('jobs', {})
    build = jobs.get('build', {})
    steps = build.get('steps', [])
    step_names = [step.get('name') for step in steps if isinstance(step, dict)]
    assert 'Checkout' in step_names
    assert any('Fetch CoinGecko markets' == name for name in step_names)
