_base_ = 'datasets'
# dataset settings
data_type = 'Grounding'
data_root = '/home/atuin/v100dd/v100dd19/FlashVTG/internvideo2/'
feat_root = '/home/atuin/v100dd/v100dd19/Videos/feature_dir/ovis/'
data = dict(
    train=dict(
        type='RepeatDataset',
        times=4,
        dataset=dict(
            type=data_type,
            label_path=data_root + 'ovis_train_release.jsonl',
            cache_path=feat_root + 'clip_ovis',
            query_path=feat_root + 'clip_text_ovis',
            use_cache=True,
            min_video_len=5,
            fps=1,
            unit=2),
        loader=dict(batch_size=8, num_workers=4, pin_memory=True, shuffle=True)),
    val=dict(
        type=data_type,
        label_path=data_root + 'ovis_val_release.jsonl',
        cache_path=data_root + 'clip_ovis',
        query_path=data_root + 'clip_text_ovis',
        use_cache=True,
        fps=1,
        unit=2,
        loader=dict(batch_size=1, num_workers=4, pin_memory=True, shuffle=False)))
