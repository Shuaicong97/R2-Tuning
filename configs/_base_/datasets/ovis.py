_base_ = 'datasets'
# dataset settings
data_type = 'Grounding'
data_root = '/home/atuin/v100dd/v100dd19/FlashVTG/internvideo2'
feat_root = '/home/atuin/v100dd/v100dd19/FlashVTG_sf_clip/final_version_slowfast_clip'
data = dict(
    train=dict(
        type='RepeatDataset',
        times=4,
        dataset=dict(
            type=data_type,
            label_path=data_root + 'ovis_train_release.jsonl',
            cache_path=feat_root + 'clip_features_ovis',
            query_path=feat_root + 'clip_text_features_ovis',
            use_cache=True,
            min_video_len=5,
            fps=0.5,
            unit=2),
        loader=dict(batch_size=128, num_workers=4, pin_memory=True, shuffle=True)),
    val=dict(
        type=data_type,
        label_path=data_root + 'ovis_val_release.jsonl',
        cache_path=data_root + 'clip_features_ovis',
        query_path=data_root + 'clip_text_features_ovis',
        use_cache=True,
        fps=0.5,
        unit=2,
        loader=dict(batch_size=1, num_workers=4, pin_memory=True, shuffle=False)))
