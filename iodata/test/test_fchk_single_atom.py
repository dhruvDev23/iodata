from importlib.resources import as_file, files
from numpy.testing import assert_allclose
from ..api import load_many

def load_fchk_trj_helper(fn_fchk):
    """Load a trajectory from a testing fchk file with iodata.iodata.load_many."""
    with as_file(files("iodata.test.data").joinpath(fn_fchk)) as fn:
        return list(load_many(fn))

def test_load_fchk_single_atom_optimization():
    """Test loading a single-atom optimization (missing trajectory block)."""
    trj = load_fchk_trj_helper("atom_opt.fchk")
    # Should load exactly one frame
    assert len(trj) == 1
    mol = trj[0]
    
    # Check basic properties
    assert mol.natom == 1
    assert mol.atnums[0] == 1
    assert mol.atcorenums[0] == 1.0
    
    # Check fallback values
    assert mol.extra["ipoint"] == 0
    assert mol.extra["npoint"] == 1
    assert mol.extra["istep"] == 0
    assert mol.extra["nstep"] == 1
    
    # Check that properties were correctly loaded from the single frame
    assert mol.energy is not None
    assert_allclose(mol.energy, -4.665818503844346e-01)
    
    # Check coordinates
    assert_allclose(mol.atcoords, [[0.0, 0.0, 0.0]])
