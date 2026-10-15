def test_imports():
    import probabilis as pb
    from probabilis import cop, emg, imu, plotting, utils
    assert callable(pb.resumo)
    assert callable(emg.filt_emg)
