# runtime settings
hooks = dict(
    type='EvalHook',
    high_keys=[
        'MR-full-mAP', 'MR-full-mIoU', 'HL-min-VeryGood-mAP', 'MR-full-R1@0.1',
        'MR-full-R1@0.3', 'MR-full-R1@0.5', 'mAP'
    ])
